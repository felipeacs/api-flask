"""
API flask completa
1 - Implementar API para incluir novos DEVs e seus conhecimentos
2- Manipular a lista
"""
import json

from flask import Flask, jsonify, request

app = Flask(__name__)

developers = [
    {'id': 0,
     'nome': 'Felipe',
     'habilidades': ['Python', 'Django', 'PL/SQL']},
    {'id': 1,
     'nome': 'Augusto',
     'habilidades': ['Python', 'Oracle', 'Flask']}
]


@app.route('/get-dev-id/<int:id>/', methods=['GET'])
def get_developer(id):
    developer = developers[id]
    return jsonify(developer)


@app.route('/edit-dev-id/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def edit_developer(id):
    # retorna, altera e deleta um desenvolvedor pelo ID
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            msg = 'Desenvolvedor de ID {} não existe!'.format(id)
            response = {'status': 'erro', 'mensagem': msg}
        except Exception:
            msg = 'Erro desconhecido. Procure o administrador da API.'
            response = {'status': 'erro', 'mensagem': msg}
        return jsonify(response)
    elif request.method == 'PUT':
        data = json.loads(request.data)
        developers[id] = data
        return jsonify(developers[id])
    elif request.method == 'DELETE':
        developers.pop(id)
        response = {'status': 'sucesso', 'mensagem': 'registro {} excluido com sucesso!'.format(id)}
        return jsonify(response)


@app.route('/dev/', methods=['POST', 'GET'])
def list_developer():
    if request.method == 'POST':
        data = json.loads(request.data)
        posicao = len(developers)
        data['id'] = posicao
        developers.append(data)
        msg = 'Registro {} inserido'.format(posicao)
        response = {'status': 'sucesso', 'mensagem': msg}
        return jsonify(response)
    elif request.method == 'GET':
        return jsonify(developers)


if __name__ == '__main__':
    app.run(debug=True)
