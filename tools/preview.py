"""Local-only static preview, including Cloudflare Pages-style clean URLs."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlsplit, unquote
import argparse

ROOT = Path(__file__).resolve().parents[1]
class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)
    def translate_path(self, path):
        resolved = Path(super().translate_path(path))
        if not resolved.exists() and not resolved.suffix and resolved.with_suffix('.html').is_file():
            return str(resolved.with_suffix('.html'))
        return str(resolved)
    def send_head(self):
        path = unquote(urlsplit(self.path).path)
        if any(part.startswith('.') for part in Path(path).parts) or path.startswith('/tools/'):
            self.send_error(404); return None
        if path.endswith('.html') and path != '/404.html':
            target = path[:-10] if path.endswith('index.html') else path[:-5]
            target = target or '/'
            self.send_response(301); self.send_header('Location', target); self.end_headers(); return None
        return super().send_head()
    def list_directory(self, path):
        self.send_error(404); return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args()
    print(f'Local: http://127.0.0.1:{args.port}', flush=True)
    ThreadingHTTPServer(('127.0.0.1', args.port), Handler).serve_forever()
