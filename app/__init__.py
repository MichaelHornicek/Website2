from flask import Flask
from .db import init_db
from .auth import auth as auth_blueprint
from .main import bp as main_blueprint

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    init_db(app)

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    return app