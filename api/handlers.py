import sys
import falcon
from falcon.media.validators import jsonschema as jsonschema
import banco

if __name__ == "__main__":
    print("Este arquivo é um módulo, e portanto não deve ser executado.")
    sys.exit(1)

class Handler(object):
    desc = "Classe base para os outros handlers."
    usage = "GET"
    route = "/null"
    db = None

    def __init__(self, database):
        self.db = database

class Colaborador(Handler):
    desc = "Classe para manipulações na tabela Colaborador."
    usage = "GET retorna todos, POST cria um"
    route = "/colaborador"

    post_schema = {
        "type": "object",
        "title": "Inserção de Colaborador via POST.",
        "description": "Informação de um Colaborador a ser adicionada.",
        "properties": {
            "id_colaborador": {
                "type": "integer",
                "description": "Identificação única do colaborador no banco de dados",
                "length": 6
            },
            "nome_colaborador": {
                "type": "string",
                "description": "O nome do colaborador",
                "minLength": 1
            },
        },
        "required": ["id_colaborador", "nome_colaborador"]
    }
    
    def on_get(self, req, resp):
        resp.media = self.db.get_colaboradores()

    @jsonschema.validate(post_schema)
    def on_post(self, req, resp):
        self.db.add_colaborador(
            resp.media.get("idColaborador"),
            resp.media.get("nomeColaborador")
        )

class Produto(Handler):
    desc = "Classe para manipulações na tabela Produto."
    usage = "GET retorna todos, POST cria um"
    route = "/produto"

    post_schema = {
        "type": "object",
        "title": "Criação de um Produto no banco de dados via POST.",
        "properties": {
            "idProduto": {
                "type": "integer",
                "description": "Identificação única do produto no estoque",
                "length": 6
            },
            "nome": {
                "type": "string",
                "description": "O nome do produto",
                "minLength": 1
            },
            "preco": {
                "type": "money",
                "description": "O preço associado ao produto",
            }
        },
        "required": ["idProduto", "nome", "preco"]
    }

    def on_get(self, req, resp):
        resp.media = self.db.get_produtos()

    @jsonschema.validate(post_schema)
    def on_post(self, req, resp):
        self.db.add_produtos(
            resp.media.get("idProduto"),
            resp.media.get("nomeProduto"),
            resp.media.get("precoProduto"),
            resp.media.get("qtdProduto")
        )

class Venda(Handler):
    desc = "Classe para manipulações na tabela Venda."
    usage = "GET retorna todas, POST cria uma, PUT atualiza uma"
    route = "/venda"
    
    post_schema = {
        "type": "object",
        "title": "Inserção de venda via POST.",
        "description": "Informação de uma venda a ser adicionada.",
        "properties": {
            "matricula": {
                "type": "integer",
                "description": "O id do colaborador associado à venda"
            },
            "valorTotal": {
                "type": "money",
                "description": "O valor total da venda"
            },
            "idQtdProdutos": {
                "type": "object",
                "description": "JSON que associa cada idProduto à quantidade vendida"
            }

        },
        "required": ["idVenda, dataVenda, valorTotal, matricula"]
    }
    
    def on_get(self, req, resp):
        resp.media = self.db.get_vendas()

    @jsonschema.validate(post_schema)
    def on_post(self, req, resp):
        self.db.add_venda(
            resp.media.get("matricula"),
            resp.media.get("valorTotal"),
            resp.media.get("idQtdProdutos")
        )
    
    def on_put(self, req, resp):
        self.db.altera_venda(
            resp.media.get("idVenda"),
            resp.media.get("matriculaColaborador"),
            resp.media.get("dataVenda"),
            resp.media.get("valor"),
            resp.media.get("quantidade"),
        )

    def on_delete(self, req, resp):
        self.db.deleta_venda(
            resp.media.get("idVenda")
        )
