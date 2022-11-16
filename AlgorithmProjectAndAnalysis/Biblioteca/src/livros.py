from flask import Flask, request, jsonify
from shared.helpers import cursor_get, cursor_post, cursor_delete

app = Flask(__name__)

TABLE = 'livros'
DATABASE = 'db-livros.db'


@app.route(f'/api/{TABLE}', methods=["GET", "POST"])
@app.route(f'/api/{TABLE}/<id_livro>', methods=["GET", "DELETE"])
def get_clientes(id_livro = None):
    # Método Get
    if request.method == "GET":
        if id_livro is not None:
            sql = f'''SELECT * FROM {TABLE} WHERE id = {id_livro}'''
        else:
            sql = f'''SELECT * FROM {TABLE}'''
        return cursor_get(sql, DATABASE)
    # Método Post
    if request.method == "POST":
        dados = request.get_json()
        if dados is not None:
            sql = f'''INSERT INTO {TABLE} (nome, 
                                            quantidade, 
                                            vendedor_id, 
                                            cliente_id, 
                                            valor, 
                                            editora_id, 
                                            edicao) 
                    VALUES ({dados['nome']}, 
                            {dados['quantidade']}, 
                            {dados['vendedor_id']},
                            {dados['cliente_id']}, 
                            {dados['valor']}, 
                            {dados['editora_id']}, 
                            {dados['edicao']})'''
            return cursor_post(sql, DATABASE)
        else:
            return jsonify({'mensagem': 'Nenhum dado foi informado!'})
    # Método Delete
    if request.method == "DELETE":
        sql = f'''DELETE FROM {TABLE} WHERE id = {id_livro}'''
        return cursor_delete(sql, DATABASE)

@app.errorhandler(404)
def endpoint_nao_encontrado(e):
    return jsonify({'mensagem': 'erro - endpoint nao encontrado'}), 404

@app.errorhandler(405)
def endpoint_nao_encontrado(e):
    return jsonify({'mensagem': 'erro - endpoint nao encontrado'}), 405


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8084', debug=True)