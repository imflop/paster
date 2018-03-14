from domain import db
from domain.models import Paster


def create_paster(data):
    title = data.get('title')
    code = data.get('code')
    paste = Paster(title=title, code=code)
    db.session.add(paste)
    db.session.commit()


def delete_paster(paster_id):
    paster = Paster.query.filter(Paster.id == paster_id).one()
    db.session.delete(paster)
    db.session.commit()


def update_paster(paster_id, data):
    paster = Paster.query.filter(Paster.id == paster_id).one()
    paster.title = data.get('title')
    paster.code = data.get('code')
    db.session.add(paster)
    db.session.commit()
