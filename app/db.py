import sqlite3, os
DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
def conn(name):
    """Cada módulo tem seu próprio banco (Estoque DB, Histórico de vendas DB, Pagamento DB)."""
    os.makedirs(DIR, exist_ok=True)
    c = sqlite3.connect(os.path.join(DIR, name + ".db"))
    c.row_factory = sqlite3.Row
    return c
