from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

def get_user_by_email(username):
    return User.query.filter_by(username=username).first()

def create_user(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()