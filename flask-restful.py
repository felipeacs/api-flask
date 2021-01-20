import json

from flask import Flask, request
from flask_restful import Resource, Api

from skils import Skils, Habilidades

app = Flask(__name__)
api = Api(app)

developers = [
    {'id': 0,
     'nome': 'Felipe',
     'habilidades': ['Python', 'Django', 'PL/SQL']},
    {'id': 1,
     'nome': 'Augusto',
     'habilidades': ['Python', 'Oracle', 'Flask']}
]


class ListDevelopers(Resource):
    def get(self):
        return developers

    def post(self):
        data = json.loads(request.data)
        posicao = len(developers)
        data['id'] = posicao
        developers.append(data)
        return developers[posicao]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = developers[id]
        except IndexError:
            msg = 'Desenvolverdor de ID {} não existe na base de dados'.format(id)
            response = {'status': 'Error', 'msg': msg}
        except Exception:
            msg = 'Erro interno na Api, entre em contato com o ADM.'
            response = {'status': 'Erro', 'msg': msg}
        return response

    def put(self, id):
        data = json.loads(request.data)
        developers[id] = data
        return data

    def delete(self, id):
        developers.pop(id)
        response = {'status': 'Sucesso', 'msg': 'Registro excluído'}
        return response


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListDevelopers, '/dev/')
api.add_resource(Skils, '/skils/')
api.add_resource(Habilidades, '/skils/<int:id>/')


if __name__ == '__main__':
    app.run(debug=True)
