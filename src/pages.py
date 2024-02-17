from flask import Blueprint

pages = Blueprint('pages', __name__)

@pages.route('/')
def index():
    return

@pages.route('/login')
def login():
    return

@pages.route('/home')
def home():
    return

@pages.route('/logout')
def logout():
    return