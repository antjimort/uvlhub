from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validatores


class NotepadForm(FlaskForm):
    submit = SubmitField('Save notepad')
