from flask import Flask 
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy 
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()

def server():
    app = Flask(__name__, template_folder="public" , static_url_path='/static')
    app.config['SECRET_KEY'] = f'{os.getenv("secret")}'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{os.getenv("db_uri")}'

    db.init_app(app)

    from .views import views
    from .auth import auth
    app.register_blueprint(views)
    app.register_blueprint(auth)

    from .db_custom import User

    with app.app_context():
        create_db()

    manager = LoginManager()
    manager.init_app(app)
    manager.login_view = 'auth.login'

    @manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app 

def create_db():
    if not os.path.exists('pack/database.db'):
        db.create_all()
        print('Database Created')

