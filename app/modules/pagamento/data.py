# Camada de DADOS - Pagamento DB
from db import conn
def init():
    with conn("pagamento") as c:
        c.execute("create table if not exists pagamentos(id integer primary key, pedido_id integer, valor real, metodo text, status text)")
def salvar(pedido_id, valor, metodo, status):
    with conn("pagamento") as c:
        return c.execute("insert into pagamentos(pedido_id,valor,metodo,status) values(?,?,?,?)", (pedido_id, valor, metodo, status)).lastrowid
def listar():
    with conn("pagamento") as c:
        return [dict(r) for r in c.execute("select * from pagamentos order by id desc")]
