from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField



class NotepadForm(FlaskForm):
    submit = SubmitField('Save notepad')
