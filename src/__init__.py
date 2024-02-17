from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .api import api
from .pages import pages

app = Flask(__name__)

db = SQLAlchemy()

app.register_blueprint(pages)

if __name__ == "__main__":
    app.run()