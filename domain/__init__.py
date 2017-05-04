from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def reset_database():
    from domain.models import Paster
    db.drop_all()
    db.create_all()
