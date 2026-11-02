# Livraria MVP — Monólito Modular
Rodar: `python3 app/main.py` → http://localhost:8000 (só Python 3.8+, sem dependências).

## Arquitetura (espelha o diagrama)
- **Front-end** (`app/static/index.html`): Navegação, Carrinho, Histórico de compras
- **API Gateway** (`app/gateway.py`): roteia `/api/<modulo>/...`
- **Módulos** (`app/modules/`), cada um com `application.py` (rotas) → `business.py` (regras) → `data.py` (banco próprio):
  - `estoque` → Estoque DB · `vendas` → Histórico de vendas DB · `pagamento` → Pagamento DB
- Módulos só se comunicam pela interface pública do `__init__.py` (facilita extrair para microsserviços depois).
- Checkout: reserva estoque → cria pedido → cobra → se recusado, repõe estoque (compensação).

## API
GET /api/estoque/livros?q= · POST /api/vendas/checkout · GET /api/vendas/historico?cliente= · GET /api/pagamento/pagamentos
Cartão terminado em `0000` simula recusa.
