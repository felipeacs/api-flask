import json

from flask import request
from flask_restful import Resource

list_skils = ['Java', 'DotNet', 'R', 'PHP', 'Pyhton']


class Skils(Resource):
    def get(self):
        return list_skils

    def post(self):
        data = json.loads(request.data)
        if any(il.lower() == str(data).lower() for il in list_skils):
            msg = 'Registro já existente'
        else:
            list_skils.append(str(data).capitalize())
            msg = 'Registro inserido'
        response = {'status': 'Sucesso', 'msg': msg}
        return response


class Habilidades(Resource):
    def put(self, id):
        data = json.loads(request.data)
        list_skils[id] = data
        return data

    def delete(self, id):
        list_skils.pop(id)
        response = {'status': 'Sucesso', 'msg': 'Registro excluído'}
        return response
