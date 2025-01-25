from flask import Flask, Blueprint, render_template
from .db import init_db
from .auth import auth as auth_blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    
    init_db(app)
    
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)