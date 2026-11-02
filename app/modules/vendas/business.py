# Camada de NEGÓCIOS - Gerenciar vendas (orquestra Estoque e Pagamento via interfaces públicas)
from . import data
from .. import estoque, pagamento
def checkout(cliente, itens, metodo, cartao=""):
    if not cliente: raise ValueError("Informe o cliente")
    if not itens: raise ValueError("Carrinho vazio")
    reservados = estoque.reservar(itens)
    total = round(sum(i["preco"] * i["qtd"] for i in reservados), 2)
    pedido_id = data.criar(cliente, total, reservados)
    pg = pagamento.cobrar(pedido_id, total, metodo, cartao)
    if pg["status"] != "aprovado":
        estoque.repor(reservados)          # compensação
        data.atualizar_status(pedido_id, "cancelado")
        return {"pedido_id": pedido_id, "status": "cancelado", "motivo": "pagamento recusado"}
    data.atualizar_status(pedido_id, "pago")
    return {"pedido_id": pedido_id, "status": "pago", "total": total}
