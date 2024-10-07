from app import db


class Notepad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.

    def __repr__(self):
        return f'Notepad<{self.id}>'
