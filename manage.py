from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from domain import db
from app import app, configure_app


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    configure_app(app)
    manager.run()
