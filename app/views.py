from flask import Blueprint, Flask, render_template, request, redirect, \
    url_for, jsonify
import datetime
import os
# Database model
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Application, Suggestions
from flask import session as login_session
from controllers import *
from forms import ApplicationAddForm, ApplicationEditForm
apply_blueprint = Blueprint('app', __name__)
suggest_blueprint = Blueprint('suggest', __name__)


@apply_blueprint.route('/')
def home():
    return render_template('applications.html', applications=get_applications())


@apply_blueprint.route('/add/application', methods=['GET', 'POST'])
def add_app():
    form = ApplicationAddForm()
    if request.method == 'POST':

        doa = map(int, request.form['date_apply'].split('-'))
        date_apply = datetime.date(doa[0], doa[1], doa[2])
        applcation = Application(company_name=request.form['company_name'],
                                 date_apply=date_apply,
                                 position=request.form['position'],
                                 job_type=request.form['job_type'],
                                 location=request.form['location'],
                                 industry=request.form['industry'],
                                 next_step=request.form['next_step'],
                                 contact=request.form['contact'],
                                 job_board=request.form['job_board'],
                                 notes=request.form['notes'])
        session.add(applcation)
        session.commit()
        return redirect(url_for('app.home'))
    else:
        return render_template('addApply.html', form=form)


@apply_blueprint.route('/edit/application/<int:id>', methods=['POST', 'GET'])
def edit_app(id):
    form = ApplicationEditForm()
    app = get_application(id)
    if request.method == 'POST':
        doa = map(int, request.form['date_apply'].split('-'))
        date_apply = datetime.date(doa[0], doa[1], doa[2])
        app.company_name = request.form['company_name']
        app.date_apply = date_apply
        app.position = request.form['position']
        app.job_type = request.form['job_type']
        app.location = request.form['location']
        app.industry = request.form['industry']
        app.next_step = request.form['next_step']
        app.contact = request.form['contact']
        app.job_board = request.form['job_board']
        app.notes = request.form['notes']
        session.add(app)
        session.commit()
        return redirect(url_for('app.home'))
    else:
        return render_template('editApply.html',
                               apply=app,
                               form=form)


@apply_blueprint.route('/info/<int:app_id>')
def more_info(app_id):
    return render_template('moreInfo.html', app=get_application(app_id))


@suggest_blueprint.route('/')
def home():
    return render_template('suggestions.html', suggestions=get_suggestions())


@suggest_blueprint.route('/add/suggestion', methods=['GET', 'POST'])
def add_suggest():
    if request.method == 'POST':
        suggestion = Suggestions(position=request.form['position'],
                                 location=request.form['location'],
                                 url=request.form['url'],
                                 suggested_by=request.form['suggested_by'])
        session.add(suggestion)
        session.commit()
        return redirect(url_for('suggest.home'))
    else:
        return render_template('modifySuggest.html', type='add')
