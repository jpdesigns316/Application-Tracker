from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, PasswordField, SelectField
from wtforms.validators import DataRequired, Required
import datetime


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class ApplicationForm(FlaskForm):
    today = datetime.date.today
    job_types = [(1, 'Full Time'), (2, 'Past Time'),
                 (3, 'Contract'), (4, 'Internship')]
    company_name = StringField('Company Name', validators=[DataRequired()])
    date_apply = DateField('Date Applied', validators=[DataRequired(
    )], format='%Y-%m-%d', default=datetime.date(today().year, today().month, today().day))
    position = StringField('Position', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    job_type = SelectField(choices=job_types, default=['1'])
    industry = StringField('Industry', validators=[DataRequired()])
    next_step = StringField('next_step', validators=[DataRequired()])
    contact = StringField('contact', validators=[DataRequired()])
    job_board = StringField('job_board', validators=[DataRequired()])
    notes = TextAreaField('notes', validators=[DataRequired()])
