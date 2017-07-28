from . import db
from slugify import slugify
from datetime import datetime


class Paster(db.Model):
    __tablename__ = 'pasters'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    slug_title = db.Column(db.String(256))
    code = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    upd_date = db.Column(db.DateTime)

    def __init__(self, title, code, pub_date=None, upd_date=None):
        self.title = title
        self.code = code
        self.slug_title = slugify(title)
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        if upd_date is None:
            upd_date = datetime.utcnow()
        self.upd_date = upd_date

    def __repr__(self):
        return '<Paste {}>'.format(self.title)
