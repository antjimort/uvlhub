from flask_wtf import FlaskForm
from wtforms import SubmitField, String


class NotepadForm(FlaskForm):
    submit = SubmitField('Save notepad')
