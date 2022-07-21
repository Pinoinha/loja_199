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
            "matricula": {
                "type": "integer",
                "description": "Identificação única do colaborador no banco de dados",
                "length": 6
            },
            "nome": {
                "type": "string",
                "description": "O nome do colaborador",
                "minLength": 1
            },
        },
        "required": ["matricula", "nome"]
    }
    
    def on_get(self, req, resp):
        resp.media = self.db.get_colaboradores()

#    @jsonschema.validate(post_schema)
    def on_post(self, req, resp):
        self.db.add_colaborador(
            req.media.get("matricula"),
            req.media.get("nome")
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

#    @jsonschema.validate(post_schema)
    def on_post(self, req, resp):
        self.db.add_produto(
            req.media.get("nomeProduto"),
            req.media.get("precoProduto"),
        )

class Venda(Handler):
    desc = "Classe para manipulações na tabela Venda."
    usage = "GET retorna todas, POST cria uma"
    route = "/venda"
    
    post_schema = {
        "type": "object",
        "title": "Inserção de venda via POST.",
        "description": "Venda realizada.",
        "properties": {
            "matricula": {
                "type": "integer",
                "description": "O id do colaborador associado à venda"
            },
            "valorTotal": {
                "type": "integer",
                "description": "Valor total da venda realizada"
            }
        },
        "required": ["matricula", "valorTotal"]
    }
    
    def on_get(self, req, resp):
        resp.media = self.db.get_vendas()

#    @jsonschema.validate(post_schema)
    def on_post(self, req, resp):
        self.db.add_venda(
            req.media.get("matricula"),
            req.media.get("valorTotal"),
            req.media.get("idQtdProdutos")
        )

class Presenca(Handler):
    desc = "Classe para manipulações na tabela Presenca."
    usage = "GET retorna todas, POST cria uma"
    route = "/presenca"
    
    post_schema = {
        "type": "object",
        "title": "Inserção de presença via POST.",
        "description": "Presença de um funcionário.",
        "properties": {
            "matricula": {
                "type": "integer",
                "description": "O id do colaborador associado à venda"
            },
            "condicao": {
                "type": "boolean",
                "description": "Se o funcionário está presente ou não"
            }

        },
        "required": ["matricula", "condicao"]
    }
    
    def on_get(self, req, resp):
        resp.media = self.db.get_presencas()

#    @jsonschema.validate(post_schema)
    def on_post(self, req, resp):
        self.db.add_presenca(
            req.media.get("matricula"),
            req.media.get("condicao")
        )
