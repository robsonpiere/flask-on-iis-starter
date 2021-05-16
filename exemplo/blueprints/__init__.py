from flask import Flask
from .main import main_blueprint

def init_blueprints(app: Flask):
    app.register_blueprint(main_blueprint)