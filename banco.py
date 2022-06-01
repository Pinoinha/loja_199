import sys
import os
import psycopg2

if __name__ == "__main__":
    print("Este arquivo é um módulo, e portanto não deve ser executado.")
    sys.exit(1)

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

    def lista_colaboradores(self):
        '''Lista os colaboradores da loja.'''
        c = self.conn.cursor()

        c.execute("SELECT matricula, tipoColaborador, nome FROM Colaborador")

        return list(map(dict, c.fetchall()))

    def lista_vendas(self):
        '''Lista as vendas da loja.'''
        c = self.conn.cursor()
        
        c.execute(
            "SELECT idVenda, dataVenda, valorTotal, matricula, Colaborador.nome
            FROM Venda
            INNER JOIN Colaborador
            ON Venda.matricula = Colaborador.matricula"
        )
        return list(map(dict, c.fetchall()))

    def lista_produtos(self):
        '''Lista os produtos na loja, junto com a quantidade em estoque de cada um.'''
        c = self.conn.cursor()

        c.execute(
            "SELECT idProduto, nome, preco, quantidadeEstoque, Venda.idVenda, Venda.dataVenda
            FROM Produto
            INNER JOIN ProdutoVenda AS pv
            ON Produto.idProduto = pv.idProduto
            INNER JOIN Venda as v
            ON pv.idVenda = v.idVenda"
        )
        return list(map(dict, c.fetchall()))

    def consulta_venda(self, idVenda):
        '''Verifica se uma venda foi registrada no banco de dados a partir de sua identificação.'''
        c = self.conn.cursor()

        try: 
            c.execute(
                f"SELECT matricula, idVenda
                FROM Venda
                WHERE idVenda={idVenda}"
            )
            return c.fetchone()
        except ProgrammingError as error:
            print(error)
            print(f'Venda {idVenda} não encontrada.')
            sys.exit(1)

    def deleta_venda(self):
        '''Deleta uma venda do banco de dados.'''
