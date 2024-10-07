from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class NotepadForm(FlaskForm):
    title = StringF
    submit = SubmitField('Save notepad')
