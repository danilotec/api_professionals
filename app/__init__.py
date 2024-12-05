from flask import Flask
from settings import SECRET_KEY

def create_app():
    app = Flask(__name__)
    app.settings['SECRET_KEY'] = SECRET_KEY

    from app.routes import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app