from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from .db import get_user_by_email, create_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = get_user_by_email(email)

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', category='success')
            return redirect(url_for('main.index'))
        else:
            flash('Login failed. Check your email and password.', category='error')

    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', category='success')
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='sha256')
        create_user(email, hashed_password)
        flash('Account created successfully!', category='success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')