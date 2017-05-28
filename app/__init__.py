from flask import Flask, render_template, request, make_response, redirect, \
    url_for, session, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Application, Suggestions
from controllers import *
import os
from forms import LoginForm

from flask import session as login_session

from views import *

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']

# Register Flask Blueprints
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
admin = app.config['USERNAME']
password = app.config['PASSWORD']
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app.register_blueprint(apply_blueprint, url_prefix='/app')
app.register_blueprint(suggest_blueprint, url_prefix='/suggest')


@app.route('/')
def home():
    return redirect(url_for('app.home'))


# route for handling the login page logic


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if request.method == 'POST':
        if (request.form['username'] != app.config['USERNAME']) \
                or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again.'
        else:
            login_session['username'] = 'Admin'
            flash('You were logged in.')
            return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    login_session.clear()
    return redirect(url_for('home'))


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'username' in login_session:
        return render_template('adminPanel.html', config=get_meta('name'))
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(port=6969)
