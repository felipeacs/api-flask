"""
Primeira API Flask
"""
import json

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/<int:id>')
def get_person(id):
    dados = {'id': id,
             'nome': 'Felipe',
             'profissao': 'Analista de sistemas'}
    return jsonify(dados)


@app.route('/soma/<int:valor1>/<int:valor2>/')
def get_soma(valor1, valor2):
    return jsonify({'soma': valor1 + valor2})


@app.route('/post-soma/', methods=['POST', 'GET'])
def post_soma():
    total = 0
    if request.method == 'POST' and request.data:
        input_data = json.loads(request.data)
        total = sum(input_data['valores'])
    elif request.method == 'GET':
        total = 1 + 0
    return jsonify({'soma': total})


if __name__ == '__main__':
    app.run(debug=True)
