from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .database import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    uname = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=uname).first()
    if user is None or not check_password_hash(user.password, password):
        return redirect(url_for('auth.login'))

    login_user(user)
    return redirect(url_for('pages.home'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    uname = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')

    user = User.query.filter_by(username=uname).first()
    if user is not None:
        return redirect(url_for('auth.signup'))

    new_user = User(username=uname, password=generate_password_hash(password, method="pbkdf2"), role=role)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/login')