from flask import Flask
from sqlalchemy import Column, ForeignKey, Integer, String, Text,  \
    UniqueConstraint, Date, func
from sqlalchemy.ext.declarative import declarative_base
import os
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']

Base = declarative_base()


class Application(Base):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True, nullable=False)
    company_name = Column(String)
    date_apply = Column(Date, default=func.now())
    position = Column(String)
    job_type = Column(String)
    location = Column(String)
    next_step = Column(String)
    industry = Column(String)
    contact = Column(String)
    job_board = Column(String)
    notes = Column(Text)

    def __init__(self, company_name, date_apply, position, job_type,
                 location, industry, next_step, contact, job_board,
                 notes):
        self.company_name = company_name
        self.date_apply = date_apply
        self.position = position
        self.location = location
        self.industry = industry
        self.next_step = next_step
        self.contact = contact
        self.job_board = job_board
        self.notes = notes

    @property
    def serialize(self):
        return {
            'id': self.id,
            'company_name': self.company_name,
            'date_apply': self.date_apply,
            'position': self.position,
            'job_type': self.job_type,
            'locaiton': self.location,
            'next_step': self.next_step,
            'contatct': self.contact,
            'job_board': self.job_board,
            'notes': self.notes
        }


class Suggestions(Base):
    __tablename__ = 'suggestions'

    id = Column(Integer, primary_key=True, nullable=False)
    position = Column(String, nullable=False)
    url = Column(String, nullable=False)
    location = Column(String, nullable=False)
    suggested_by = Column(String)

    def __init__(self, position, url, location, suggested_by):
        self.position = position
        self.url = url
        self.location = location
        self.suggested_by = suggested_by

    @property
    def seriealize():
        return{
            'id': self.id,
            'company_name': self.company_name,
            'url': self.url,
            'location': self.location,
            'suggested_by': self.suggested_by
        }


db_name = os.path.join(BASE_DIR, FILENAME + '.db')
if os.path.exists((db_name):
    os.remove(db_name)

engine=create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

Base.metadata.create_all(engine)
