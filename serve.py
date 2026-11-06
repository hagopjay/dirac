"""Serve the complete offline demo with Python 3. No packages required."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from functools import partial
import argparse, threading, webbrowser
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--port',type=int,default=8000)
parser.add_argument('--no-browser',action='store_true')
args=parser.parse_args()
handler=partial(SimpleHTTPRequestHandler,directory=str(Path(__file__).resolve().parent))
try: server=ThreadingHTTPServer(('127.0.0.1',args.port),handler)
except OSError as exc: parser.exit(1,f'Could not start on port {args.port}: {exc}\nTry --port 8001.\n')
url=f'http://localhost:{args.port}/'
print(f'Dirac: the Loom Collider\nOpen {url}\nPress Ctrl+C to stop.',flush=True)
if not args.no_browser: threading.Timer(0.8,lambda:webbrowser.open(url)).start()
try: server.serve_forever()
except KeyboardInterrupt: pass
finally: server.server_close()
