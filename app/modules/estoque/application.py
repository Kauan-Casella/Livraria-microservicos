# Camada de APLICAÇÃO - Estoque (rotas)
from . import data
def handle(method, path, body, query):
    if method == "GET" and path == "/livros":
        return 200, data.listar(query.get("q", [""])[0])
    return 404, {"erro": "rota não encontrada"}
