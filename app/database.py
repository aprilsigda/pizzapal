'''
File: database.py
Author: April Sigda
Purpose: Sets up the connection to the database backend
'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Initializes the database connection. If the
# necessary tables are not already present,
# creates them. This should be called every
# time the app is run.
# Parameters:
# - app (Flask): the Flask object representing
#       the currently running application
# Requires:
# - app.config['SECRET_KEY']
# - app.config['SQLALCHEMY_DATABASE_URI']
# (these are set up in __init__.py)
def init_db(app):
    db.init_app(app)
    from . import models
    with app.app_context():
        db.create_all()