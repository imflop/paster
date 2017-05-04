from flask import request
from flask_restplus import Resource
from api.restplus import api
from api.paster.serializers import paster
from api.paster.business import create_paster
from domain.models import Paster


ns = api.namespace('paster', description='Operations related to paste of code')


@ns.route('/')
class PastesCollection(Resource):

    @api.expect(paster)
    def post(self):
        """ Create a new paster """
        create_paster(request.json)
        return None, 201


@ns.route('/<int:id>')
@ns.param('id', 'Paster id')
@api.response(404, 'Paster not found')
class PasterItem(Resource):

    @api.marshal_with(paster)
    def get(self, id):
        """ Return a paster item by id """
        p = Paster.query.filter(Paster.id == id).one()
        return p
