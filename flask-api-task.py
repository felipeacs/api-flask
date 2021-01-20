"""
Exercicio
"""

import json

from flask import Flask, jsonify, request

app = Flask(__name__)

task_list = [
    {'id': 0,
     'responsavel': 'Felipe',
     'tarefa': 'Estudar',
     'status': 'To-Do'},
    {'id': 1,
     'responsavel': 'Augusto',
     'tarefa': 'Programar',
     'status': 'Doing'}
]


@app.route('/task/', methods=['GET', 'POST'])
def task():
    if request.method == 'GET':
        return jsonify(task_list)
    elif request.method == 'POST':
        data = json.loads(request.data)
        position = len(task_list)
        data['id'] = position
        task_list.append(data)
        msg = 'Registro {} inserido com sucesso!'.format(position)
        response = {'status': 'sucesso', 'mensagem': msg}
        return jsonify(response)


@app.route('/edit-task/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def task_edit(id):
    if request.method == 'GET':
        try:
            response = task_list[id]
        except IndexError:
            msg = 'Registro {} não encontrado!'.format(id)
            response = {'status': 'Error', 'msg': msg}
        except Exception:
            msg = 'Erro interno, procure o administrador da API.'
            response = {'status': 'Error', 'msg': msg}
        return jsonify(response)
    elif request.method == 'PUT':
        try:
            data = json.loads(request.data)
            task_list[id]['status'] = data['status']
            msg = 'Registro {}, alterado com sucesso!'.format(id)
            response = {'status': 'Sucesso', 'msg': msg}
        except IndexError:
            msg = 'Registro {} não encontrado!'.format(id)
            response = {'status': 'Error', 'msg': msg}
        except Exception:
            msg = 'Erro interno, procure o administrador da API'
            response = {'Status': 'Error', 'Msg': msg}
        return jsonify(response)
    elif request.method == 'DELETE':
        try:
            task_list.pop(id)
            msg = 'Registro {} removido com sucesso!'.format(id)
            response = {'Status': 'Sucesso', 'Msg': msg}
        except IndexError:
            msg = 'Registro {} não encontrado!'.format(id)
            response = {'Status': 'Error', 'msg': msg}
        except Exception:
            msg = 'Erro interno, procure o administrador da API!'
            response = {'status': 'Error', 'msg': msg}
        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
