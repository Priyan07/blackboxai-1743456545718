import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Available pages:")
    print(f"- Practice: http://localhost:{PORT}/practice.html")
    print(f"- Leaderboard: http://localhost:{PORT}/leaderboard.html") 
    print(f"- Progress: http://localhost:{PORT}/progress.html")
    print(f"- Question Log: http://localhost:{PORT}/log.html")
    print(f"- RC Glossary: http://localhost:{PORT}/rc_glossary.html")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")