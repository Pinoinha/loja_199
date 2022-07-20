import sys
import os
from datetime import datetime, timezone, timedelta
from uuid import uuid4
import psycopg2

if __name__ == "__main__":
    print("Este arquivo é um módulo, e portanto não deve ser executado.")
    sys.exit(0)

class Banco(object):
    def __init__(self, filename, **kwargs):
        self.user = kwargs.get("user") or "postgre"
        self.password = kwargs.get("password") or None
        self.host = kwargs.get("host") or "127.0.0.1"
        self.port = kwargs.get("port") or "5432"
        
        if not os.path.isfile(filename):
            print(f"Arquivo {filename} não existe.")
            sys.exit(1)

        self.filename = filename
        self.conn = psycopg2.connect(
            dbname = self.filename, user = self.user, password = self.password,
            host = self.host, port = self.port
        )

    def get_colaboradores(self):
        """Lista os colaboradores da loja."""
        c = self.conn.cursor()

        c.execute(
            """
            SELECT *
            FROM Colaborador;
            """
        )

        colaboradores = c.fetchall()

        if colaboradores is None:
            raise ProgrammingError("Nenhum colaborador encontrado.")
        
        return list(map(dict, c.fetchall()))
    
     def add_colaborador(self, id_colaborador, nome_colaborador):
        """Adiciona colaborador no banco de dados."""
        c = self.conn.cursor()

        if acha_duplicata_colaborador(id_colaborador):
            raise Exception(f"Colaborador com id {id_colaborador} já existe.")

        c.execute(
            """
            INSERT INTO Colaborador (id_colaborador, nome_colaborador)
            VALUES (%s, %s)
            """,
            (id_colaborador, nome_colaborador)
        )
        
        self.conn.commit()

    def get_vendas(self):
        """Lista as vendas da loja."""
        c = self.conn.cursor()
        
        c.execute(
            """
            SELECT idVenda, dataVenda, valorTotal, matricula, Colaborador.nome
            FROM Venda
            INNER JOIN Colaborador
            ON Venda.matricula = Colaborador.matricula;
            """
        )
        return list(map(dict, c.fetchall()))
    
    def consulta_venda(self, idVenda):
        """Verifica se uma venda foi registrada no banco de dados a partir de sua identificação."""
        c = self.conn.cursor()

        c.execute(
            """
            SELECT matricula, idVenda
            FROM Venda
            WHERE idVenda = %s;
            """,
            (idVenda)
        )
        
        return c.fetchone()

    def add_venda(self, matriculaColaborador, valor, quantidade, **idQtdProdutos):
        c = self.conn.cursor()
        #TODO: Verify
        idVenda = str(uuid4())[:6] # idVenda foi definido como tendo tamanho máximo de 6 caracteres
        dataVenda = datetime.now(timezone(timedelta(hours=-3)))
        
        for idProduto, quantidade in idQtdProdutos.items():
            if verifica_qtd(idProduto, quantidade) is not None:
                # isso está errado! precisa verificar *todos* os itens antes
                # TODO: consertar
            	c.execute(
                    """
                    INSERT INTO Venda (idVenda, dataVenda, valorTotal, matricula)
                    VALUES (%s, %s, %s)
                    """,
                    (idVenda, dataVenda, valor, matriculaColaborador)
                )
                
               self.conn.commit()
               
              else:
                print(f"Não há {quantidade} de produtos com o id {idProduto} dísponíveis.")
        
    def altera_venda(self, idVenda, matriculaColaborador, dataVenda, valor, quantidade):
        """Altera uma venda do banco de dados."""
        c = self.conn.cursor()
        
        c.execute(
            """EDIT matriculaColaborador, dataVenda, valor, quantidade
            FROM Venda
            WHERE idVenda = %s
            VALUES (%s, %s, %s, %s)
            """,
            (idVenda, matriculaColaborador, dataVenda, valor, quantidade)
        )
        self.conn.commit() 
        
        #TODO: Verify
        
    def deleta_venda(self, idVenda):
        """Deleta uma venda do banco de dados."""
        c = self.conn.cursor()

        c.execute(
            """
            DELETE FROM Venda
            WHERE idVenda = %s
            """,
            (idVenda)
        )
        self.conn.commit()

    def verifica_qtd(self, idProduto, quantidade):
        """Verifica se há, no banco de dados, uma quantidade suficiente de um determinado produto."""
        c = self.conn.cursor()

        c.execute(
            """
            SELECT idProduto, quantidade FROM ProdutoVenda
            WHERE idProduto = %s AND
                  quantidade >= %s
            """,
            (idProduto, quantidade)
        )
        
        produto_existe = c.fetchall() is not None

        if not produto_existe:
            raise ProgrammingError(f"Produto com id {idProduto} não encontrado.")
        
        return list(map(dict, c.fetchall()))

    def get_produtos(self):
        """Lista os produtos na loja, junto com a quantidade em estoque de cada um."""
        c = self.conn.cursor()

        c.execute(
            """
            SELECT idProduto, nome, preco, quantidadeEstoque, Venda.idVenda, Venda.dataVenda
            FROM Produto
            INNER JOIN ProdutoVenda AS pv
            ON Produto.idProduto = pv.idProduto
            INNER JOIN Venda as v
            ON pv.idVenda = v.idVenda;
            """
        )
        
        return list(map(dict, c.fetchall()))

    def add_produto(self, idProduto, nomeProduto, precoProduto, qtdProduto):
        """Adiciona produto no estoque."""
        c = self.conn.cursor()

        if acha_duplicata_produto(idProduto):
            raise Exception(f"Produto com id {id_produto} já existe.")
        
        c.execute(
            """
            INSERT INTO Produto (idProduto, nomeProduto, precoProduto)
            VALUES (%s, %s, %s)
            """,
            (idProduto, nomeProduto, precoProduto)
        )
        
        self.conn.commit()
        
    def acha_duplicata_produto(self, idProduto):
        """Encontra produtos duplicados no estoque."""
        c = self.conn.cursor()

        c.execute(
            """
            SELECT idProduto
            FROM Produto
            WHERE idProduto = %s
            """,
            (idProduto,)
        )
    
        return c.fetchone() is not None
    
    def acha_duplicata_colaborador(self, id_colaborador):
        """Encontra colaborador duplicado no banco de dados."""
        c = self.conn.cursor()

        c.execute(
            """
            SELECT id_colaborador
            FROM Colaborador
            WHERE id_colaborador = %s
            """,
            (id_colaborador,)
        )
    
        return c.fetchone() is not None
