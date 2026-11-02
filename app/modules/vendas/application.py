# Camada de APLICAÇÃO - Gerenciar vendas
from . import data, business
def handle(method, path, body, query):
    try:
        if method == "POST" and path == "/checkout":
            return 201, business.checkout(body.get("cliente"), body.get("itens", []), body.get("metodo", "pix"), body.get("cartao", ""))
        if method == "GET" and path == "/historico":
            return 200, data.historico(query.get("cliente", [""])[0])
    except ValueError as e:
        return 400, {"erro": str(e)}
    return 404, {"erro": "rota não encontrada"}
