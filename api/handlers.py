import sys
import falcon
from falcon.media.validators import jsonschema as jsonschema

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

class Help(Handler):
    desc = "Classe para documentação da API."
    usage = "GET retorna informações sobre todos os handlers."
    route = "/"
    instances = {}

    def add_handler(self, name, new_handler):
        """Adiciona um handler à lista de instâncias do objeto"""
        self.instances[name] = {
            "descricao": new_handler.desc,
            "uso": new_handler.usage,
            "rota": new_handler.route
        }

    def on_get(self, req, resp):
        resp.media = self.instances

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
                "type": "string",
                "description": "Matrícula do colaborador"
            },
            "nome": {
                "type": "string",
                "description": "Nome completo do colaborador"
            },
            "dataAdmissao": {
                "type": "date",
                "description": "Data de admissão do colaborador na empresa"
            },
            "salarioBruto": {
                "type": "money",
                "description": "Salário bruto do colaborador"
            },
            "salarioLiquido": {
                "type": "money",
                "description": "Salário líquido do colaborador"
p            },
            "percentualComissao": {
                "type": "float",
                "description": "Percentual de comissão que o colaborador recebe a cada venda"
            },
            "tipoColaborador": {
                "type": "attribute",
                "description": "Tipo do colaborador"
            },
            "required": ["matricula"]
        }
    }

    def on_get(self, req, resp):
        resp.media = self.db.get_colaboradores()

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
            },
        },
        "required": ["id_produto", "nome", "preco"]
    }

    def on_get(self, req, resp):
        resp.media = self.db.get_produtos()

    # TODO
    def on_post(self, req, resp):
        pass

class Venda(Handler):
    desc = "Classe para manipulações na tabela Venda."
    usage = "GET retorna todas, POST cria uma, PUT atualiza uma"
    route = "/venda"

    post_schema = {
        "type": "object",
        "title": "Criação de uma venda através do POST"
        "properties": {
           "idVenda": {
               "type": "integer",
               "description": "Identificação única da venda no banco de dados",
               "length": 6
           }
        }
    }

    def on_get(self, req, resp):
        resp.media = self.db.get_vendas()

    @jsonschema.validate(post_schema)
    def on_post(self, req, resp):
        pass
