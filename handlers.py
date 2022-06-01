import sys
import falcon

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

# ideia kibada COMPLETAMENTE do Borges:
# a API SE AUTODOCUMENTA
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

class 
