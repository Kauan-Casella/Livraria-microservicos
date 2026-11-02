# API Gateway: único ponto de entrada, roteia /api/<modulo>/... para o módulo
from modules import estoque, vendas, pagamento
ROTAS = {"estoque": estoque, "vendas": vendas, "pagamento": pagamento}
def rotear(method, path, body, query):
    partes = path.strip("/").split("/", 1)
    mod = ROTAS.get(partes[0])
    if not mod: return 404, {"erro": "módulo desconhecido"}
    return mod.handle(method, "/" + (partes[1] if len(partes) > 1 else ""), body, query)
