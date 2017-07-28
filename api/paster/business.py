from datetime import datetime
from slugify import slugify
from domain import db
from domain.models import Paster


def create_paster(data):
    title = data.get('title')
    code = data.get('code')
    paste = Paster(title, code)
    db.session.add(paste)
    db.session.commit()


def delete_paster(paster_id):
    paster = Paster.query.filter(Paster.id == paster_id).one()
    db.session.delete(paster)
    db.session.commit()


def update_paster(paster_id, data):
    paster = Paster.query.filter(Paster.id == paster_id).one()
    paster.title = data.get('title')
    paster.slug_title = slugify(data.get('title'))
    paster.code = data.get('code')
    if data.get('pub_date') is not None:
        paster.pub_date = datetime.strptime(data.get('pub_date'),
                                            "%Y-%m-%dT%H:%M:%S.%f")
    if data.get('upd_date') is not None:
        paster.upd_date = datetime.strptime(data.get('upd_date'),
                                            "%Y-%m-%dT%H:%M:%S.%f")
    else:
        paster.upd_date = datetime.utcnow()
    db.session.add(paster)
    db.session.commit()
