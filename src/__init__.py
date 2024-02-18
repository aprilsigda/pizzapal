from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .pages import pages
from .auth import auth
from .database import db
from . import models

app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

database.init_db(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))

app.register_blueprint(pages)
app.register_blueprint(auth)

if __name__ == "__main__":
    app.run()