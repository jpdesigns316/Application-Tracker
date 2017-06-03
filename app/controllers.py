from flask import Flask
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from models import *

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']


def load_engine():
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    return engine


engine = load_engine()
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def get_applications():
    return session.query(Application).order_by(desc(Application.date_apply)).all()


def get_application(id):
    return session.query(Application).filter_by(id=id).one()


def get_suggestions():
    return session.query(Suggestions).all()


def get_suggestion(id):
    return session.query(Suggestions).filter_by(id=id).one()
