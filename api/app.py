import falcon

import handlers, banco

db = banco.Banco("/tmp/tmp.hfU0gYjhh9/banco.db", host="0.0.0.0", port=5432)

app = falcon.App()
app.add_route('/colaborador', handlers.Colaborador())
app.add_route('/produto', handlers.Produto())
app.add_route('/venda', handlers.Venda())
