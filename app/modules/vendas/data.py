# Camada de REGISTRO - Histórico de vendas DB
import json
from db import conn
def init():
    with conn("vendas") as c:
        c.execute("create table if not exists pedidos(id integer primary key, cliente text, total real, status text, itens text, criado text default current_timestamp)")
def criar(cliente, total, itens):
    with conn("vendas") as c:
        return c.execute("insert into pedidos(cliente,total,status,itens) values(?,?,?,?)", (cliente, total, "pendente", json.dumps(itens))).lastrowid
def atualizar_status(i, status):
    with conn("vendas") as c: c.execute("update pedidos set status=? where id=?", (status, i))
def historico(cliente):
    with conn("vendas") as c:
        rows = [dict(r) for r in c.execute("select * from pedidos where cliente=? order by id desc", (cliente,))]
        for r in rows: r["itens"] = json.loads(r["itens"])
        return rows
