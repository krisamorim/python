from flask import Flask, jsonify, request
app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O senhor dos aneis',
        'autor':'J.R.R.'
    },
    {
        'id': 2,
        'titulo': 'Livro 2',
        'autor':'Autor do livro 2'
    },
    {
        'id': 3,
        'titulo': 'Livro 3',
        'autor':'Autor do livro 3'
    }
]

#retorna todos
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#consulta por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#alterar livro
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
#incluir novo livro
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro)

#excluir livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)