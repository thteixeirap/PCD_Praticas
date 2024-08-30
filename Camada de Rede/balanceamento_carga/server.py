# server.py
from flask import Flask, jsonify
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return "Serviço no servidor!"

@app.route('/health')
def health_check():
    return jsonify(status="UP")

if __name__ == "__main__":
    port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port)
