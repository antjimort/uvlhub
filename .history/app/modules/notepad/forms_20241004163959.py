from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Len


class NotepadForm(FlaskForm):
    submit = SubmitField('Save notepad')
