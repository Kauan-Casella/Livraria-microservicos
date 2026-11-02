import json, os, sys
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modules import estoque, vendas, pagamento
import gateway
STATIC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "index.html")
class H(BaseHTTPRequestHandler):
    def _go(self, m):
        u = urlparse(self.path)
        if u.path.startswith("/api/"):
            n = int(self.headers.get("Content-Length") or 0)
            body = json.loads(self.rfile.read(n) or b"{}") if n else {}
            code, out = gateway.rotear(m, u.path[5:], body, parse_qs(u.query))
            data, ct = json.dumps(out).encode(), "application/json"
        else:
            code, ct, data = 200, "text/html; charset=utf-8", open(STATIC, "rb").read()
        self.send_response(code); self.send_header("Content-Type", ct)
        self.send_header("Content-Length", str(len(data))); self.end_headers(); self.wfile.write(data)
    def do_GET(self): self._go("GET")
    def do_POST(self): self._go("POST")
    def log_message(self, *a): pass
if __name__ == "__main__":
    for m in (estoque, vendas, pagamento): m.init()
    print("Livraria rodando em http://localhost:8000")
    ThreadingHTTPServer(("", 8000), H).serve_forever()
