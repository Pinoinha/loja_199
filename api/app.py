import falcon

import handlers, banco

db = banco.Banco("postgres", host="127.0.0.1", user="postgres", password="1234")

app = falcon.App()
app.add_route('/colaborador', handlers.Colaborador(db))
app.add_route('/produto', handlers.Produto(db))
app.add_route('/venda', handlers.Venda(db))
