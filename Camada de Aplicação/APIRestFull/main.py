from flask import Flask
from routes import bp as api_bp

app = Flask(__name__)

# Registrar o blueprint das rotas
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
