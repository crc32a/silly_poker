from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, HiddenField
from wtforms import SubmitField, TextField, TextAreaField
from wtforms.validators import DataRequired
import flask_wtf
import wtforms.validators
import wtforms

class LoginForm(FlaskForm):
    name = StringField("user", validators=[DataRequired()])
    project = StringField("project", validators=[DataRequired()])

