from flask import Blueprint, render_template, redirect
from flask_login import current_user

pages = Blueprint('pages', __name__)

@pages.route('/')
def index():
    return

@pages.route('/home')
def home():
    if not current_user.is_authenticated:
        return redirect('/login')
    elif current_user.role == 'chef':
        return render_template('chefhome.html')
    elif current_user.role == 'manager':
        return render_template('managerhome.html')