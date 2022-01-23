# microblog_flask
Python Microblog based on Flask  

# microblog_flask

A simple Flask web application running on your computer.

## Requirements

- Python 3.6+
- pip

## Install

- creates a virtual environment named 'venv':
$ python3 -m venv venv

- activate your brand new virtual environment:
$ source venv/bin/activate

- install Flask:
$ pip install Flask

- install Flask-WTF:
$ pip install flask-wtf

- install Flask-SQLAlchemy:
$ pip install flask-sqlalchemy

- install Flask-Migrate:
$ pip install flask-migrate

- install Flask-Migrate:
$ pip install flask-login

- install Email-validator:
$ pip install email_validator

- install Flask-Bootstrap:
$ pip install flask-bootstrap

- setting the FLASK_APP environment variable:
$ export FLASK_APP=microblog.py

- create the migration repository:
$ flask db init

- add the entire User model to the migration script:
$ flask db migrate -m "users table"

- apply the changes to the database:
$ flask db upgrade

- launch  web application:
$ flask run

