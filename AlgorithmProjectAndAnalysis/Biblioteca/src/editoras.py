from flask import Flask, request, jsonify
from producer.producer_cliente import send_message
from shared.helpers import cursor_get, cursor_post, cursor_delete

app = Flask(__name__)

TABLE = 'editoras'
DATABASE = 'db-editora.db'

@app.route(f'''/api/{TABLE}''', methods=["GET", "POST"])
@app.route(f'''/api/{TABLE}/<id>''', methods=["GET", "DELETE"])
def get(id = None):
    # Método Get
    if request.method == "GET":
        if id is not None:
            sql = f'''SELECT * FROM {TABLE} WHERE id = {id}'''
        else:
            sql = f'''SELECT * FROM {TABLE}'''
        return cursor_get(sql, DATABASE)
    # Método Post
    if request.method == "POST":
        dados = request.get_json()
        if dados is not None:
            sql = f'''
                    INSERT INTO {TABLE} (cnpj, 
                                        nome, 
                                        endereco, 
                                        numero, 
                                        bairro, 
                                        cidade, 
                                        estado, 
                                        cep, 
                                        telefone, 
                                        email ) 
                    VALUES ({dados['cnpj']}, 
                            {dados['nome']}, 
                            {dados['endereco']},
                            {dados['numero']}, 
                            {dados['bairro']}, 
                            {dados['cidade']}, 
                            {dados['estado']}, 
                            {dados['cep']},
                            {dados['telefone']}, 
                            {dados['email']})'''
                            
            dados['method'] = "POST"
            send_message(TABLE, dados)
                            
            return cursor_post(sql, DATABASE)
        else:
            return jsonify({'mensagem': 'Nenhum dado foi informado!'})
    # Método Delete
    if request.method == "DELETE":
        sql = f'''DELETE FROM {TABLE} WHERE id = {id}'''
        message = {'method': 'DELETE', 'id': id}
        send_message(TABLE, message)
        return cursor_delete(sql, DATABASE)

@app.errorhandler(404)
def endpoint_nao_encontrado(e):
    return jsonify({'mensagem': 'erro - endpoint nao encontrado'}), 404

@app.errorhandler(405)
def endpoint_nao_encontrado(e):
    return jsonify({'mensagem': 'erro - endpoint nao encontrado'}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8082', debug=True)