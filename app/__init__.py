'''
File: __init__.py
Author: April Sigda
Purpose: This is the entrypoint for the application. It sets
    up the database, login manager, and registers all the
    request handler blueprints.
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .pages import pages
from .auth import auth
from .topping import topping
from .pizza import pizza
from .database import db
from . import models, settings

app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_CONNECTION_STRING

database.init_db(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))

app.register_blueprint(pages)
app.register_blueprint(auth)
app.register_blueprint(topping)
app.register_blueprint(pizza)

if __name__ == "__main__":
    app.run()