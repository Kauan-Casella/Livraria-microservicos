# Camada de DADOS - Estoque DB
from db import conn
def init():
    with conn("estoque") as c:
        c.execute("create table if not exists livros(id integer primary key, titulo text, autor text, preco real, qtd integer)")
        if not c.execute("select 1 from livros").fetchone():
            c.executemany("insert into livros(titulo,autor,preco,qtd) values(?,?,?,?)", [
                ("Clean Architecture","Robert C. Martin",89.90,10),
                ("Domain-Driven Design","Eric Evans",129.00,5),
                ("Building Microservices","Sam Newman",110.50,7),
                ("Refactoring","Martin Fowler",99.00,8),
                ("O Programador Pragmático","Hunt & Thomas",85.00,12)])
def listar(q=""):
    with conn("estoque") as c:
        like = f"%{q}%"
        return [dict(r) for r in c.execute("select * from livros where titulo like ? or autor like ?", (like, like))]
def obter(i):
    with conn("estoque") as c:
        r = c.execute("select * from livros where id=?", (i,)).fetchone()
        return dict(r) if r else None
def ajustar(i, delta):
    with conn("estoque") as c:
        c.execute("update livros set qtd = qtd + ? where id=?", (delta, i))
