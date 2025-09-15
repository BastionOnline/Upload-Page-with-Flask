from flask import Flask
from .routes import main   # relative import works inside a package

def create_app():
    app = Flask(__name__)

    # from .routes import main
    app.register_blueprint(main)

    return app
