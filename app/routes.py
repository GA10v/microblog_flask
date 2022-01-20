from crypt import methods
from turtle import title
from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginFrom, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from app import db


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'autor': {'username':'Dima'},
            'body': 'Beautiful day in SPB'
        },
        {
            'autor': {'username': 'Alla'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'autor': {'username': 'Andrey'},
            'body': 'Test_test'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc !='':
            next_page = url_for('index')
        return redirect(url_for(next_page))
    return render_template('login.html', title='Sing In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulation, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)