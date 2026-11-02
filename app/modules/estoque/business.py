# Camada de NEGÓCIOS - Estoque
from . import data
def reservar(itens):
    """itens: [{id, qtd}] -> valida tudo, baixa estoque e devolve itens com preço."""
    resultado = []
    for it in itens:
        l = data.obter(it["id"])
        if not l: raise ValueError(f"Livro {it['id']} não existe")
        if it["qtd"] < 1 or l["qtd"] < it["qtd"]:
            raise ValueError(f"Estoque insuficiente para '{l['titulo']}'")
        resultado.append({"id": l["id"], "titulo": l["titulo"], "preco": l["preco"], "qtd": it["qtd"]})
    for r in resultado: data.ajustar(r["id"], -r["qtd"])
    return resultado
def repor(itens):
    for it in itens: data.ajustar(it["id"], it["qtd"])
