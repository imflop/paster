from . import db
from slugify import slugify
from datetime import datetime


class Paster(db.Model):
    __tablename__ = 'pasters'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    slug_title = db.Column(db.String(256), unique=True)
    code = db.Column(db.Text)
    pub_date = db.Column(db.DateTime, default=datetime.now())
    upd_date = db.Column(
        db.DateTime,
        default=datetime.now(),
        onupdate=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Paster, self).__init__(*args, **kwargs)
        self.slug_title = slugify(self.title)

    def __repr__(self):
        return '<Paste {}>'.format(self.title)
