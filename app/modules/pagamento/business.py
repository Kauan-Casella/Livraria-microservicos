# Camada de NEGÓCIOS - Pagamento (gateway simulado)
from . import data
def cobrar(pedido_id, valor, metodo, cartao=""):
    if metodo not in ("cartao", "pix"): raise ValueError("Método inválido")
    aprovado = valor > 0 and not (metodo == "cartao" and cartao.replace(" ", "").endswith("0000"))  # final 0000 = recusado
    status = "aprovado" if aprovado else "recusado"
    return {"id": data.salvar(pedido_id, valor, metodo, status), "status": status}
