from flask import Flask
from exemplo.ext import cors

def init_app(app: Flask) -> Flask:
    """
    Adiciona as configurações
    """
    cors.init_app(app)
    return app