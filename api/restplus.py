# import logging
# import traceback
import settings
from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound


api = Api(version='1.0', title='Paster API',
          description='A simple API to integrate third party stuff')


@api.errorhandler
def default_error_handler(err):
    message = 'An unhandled exception occurred.'
    # log.exception(message)

    if settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(err):
    # log.warning(traceback.format_exc())
    return {'message': 'A database result was required but was not found.'}, 404
