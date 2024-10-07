from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
fro


class NotepadForm(FlaskForm):
    submit = SubmitField('Save notepad')
