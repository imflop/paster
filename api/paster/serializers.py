from flask_restplus import fields
from api.restplus import api


paster = api.model('Paste of code', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of paste'),
    'title': fields.String(required=True, description='Paste title'),
    'code': fields.String(required=True, description='Body of code'),
    'pub_date': fields.DateTime,
    'upd_date': fields.DateTime,
})
