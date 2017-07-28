from flask import request
from flask_restplus import Resource
from api.restplus import api
from api.paster.serializers import paster
from api.paster.business import create_paster, delete_paster, update_paster
from domain.models import Paster


ns = api.namespace('paster', description='Operations related to paste of code')


@ns.route('/')
class PastesCollection(Resource):

    @api.expect(paster)
    def post(self):
        """
        Create a new paster
        :return: None or 201 status code
        """
        create_paster(request.json)
        return None, 201


@ns.route('/<int:id>')
@ns.param('id', 'Paster id')
@api.response(404, 'Paster not found')
class PasterItem(Resource):

    @api.marshal_with(paster)
    def get(self, id):
        """
        Return a paster item by id 
        :param id: id of paster
        :return: paster item
        """
        return Paster.query.filter(Paster.id == id).one()

    @api.response(204, 'Poster successfully deleted')
    def delete(self, id):
        """
        Delete poster by id
        :param id: poster id
        :return: None or 204 status code
        """
        delete_paster(id)
        return None, 204

    @api.expect(paster)
    @api.response(204, 'Paster successfully updated')
    def put(self, id):
        """
        Update paster by id
        pub_date and upd_date format is %Y-%m-%dT%H:%M:%S.%f
        :param id: paster id
        :return: None or 204 status code
        """
        update_paster(id, request.json)
        return None, 204