# load_balancer.py
from flask import Flask, request, redirect, make_response
import requests
import random

app = Flask(__name__)

# Lista de servidores
servers = ["http://localhost:5001", "http://localhost:5002"]
server_status = {server: True for server in servers}

def check_health():
    global server_status
    for server in servers:
        try:
            response = requests.get(f"{server}/health", timeout=2)
            server_status[server] = (response.status_code == 200)
        except requests.RequestException:
            server_status[server] = False

def get_available_servers():
    return [server for server in servers if server_status[server]]

def choose_server():
    available_servers = get_available_servers()
    if not available_servers:
        return None
    # Distributing based on session stickiness
    session_server = request.cookies.get('server')
    if session_server and session_server in available_servers:
        return session_server
    return random.choice(available_servers)

@app.route('/')
def index():
    check_health()
    server = choose_server()
    if server is None:
        return "Todos os servidores estão fora do ar.", 503
    resp = redirect(server, code=302)
    resp.set_cookie('server', server)
    return resp

if __name__ == "__main__":
    app.run(port=5000)
