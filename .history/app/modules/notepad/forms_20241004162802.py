from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, 


class NotepadForm(FlaskForm):
    submit = SubmitField('Save notepad')
