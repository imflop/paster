from domain import db
from domain.models import Paster


def create_paster(data):
    title = data.get('title')
    code = data.get('code')
    paste = Paster(title, code)
    db.session.add(paste)
    db.session.commit()
