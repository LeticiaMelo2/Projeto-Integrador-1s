from flask import Flask
from config import Config
from routes.usuario_routes import usuario_bp
from routes.operador_routes import operador_bp
from routes.historico_routes import historico_bp

app = Flask(__name__,
            template_folder='../Frontend/templates',
            static_folder='../Frontend/static')

app.config['SECRET_KEY'] = 'abc123'
app.config.from_object(Config)

app.register_blueprint(usuario_bp)
app.register_blueprint(operador_bp)
app.register_blueprint(historico_bp)

if __name__ == '__main__':
    app.run(debug=True)