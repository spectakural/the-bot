from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class QueryForm(FlaskForm):
    query = StringField('query')
    submit = SubmitField('submit')
    