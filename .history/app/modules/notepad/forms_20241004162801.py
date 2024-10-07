from flask_wtf import FlaskForm
from wtforms import SubmitField, StringF


class NotepadForm(FlaskForm):
    submit = SubmitField('Save notepad')
