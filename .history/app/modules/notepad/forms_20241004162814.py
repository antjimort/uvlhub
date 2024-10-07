from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.valida


class NotepadForm(FlaskForm):
    submit = SubmitField('Save notepad')
