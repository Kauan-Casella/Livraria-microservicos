# Camada de APLICAÇÃO - Pagamento
from . import data
def handle(method, path, body, query):
    if method == "GET" and path == "/pagamentos": return 200, data.listar()
    return 404, {"erro": "rota não encontrada"}
