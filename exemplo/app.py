from flask import Flask
from .ext import configuration
from .blueprints import init_blueprints

def basic_app() -> Flask:
    """
    Cria um app básico
    """
    app = Flask(__name__)
    return app

def create_app() -> Flask:
    app = basic_app()
    configuration.init_app(app)
    init_blueprints(app)
    return app