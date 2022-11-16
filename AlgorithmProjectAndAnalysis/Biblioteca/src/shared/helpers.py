if __name__ == "__main__":
    ...
else:
        
    import sqlite3 as sql
    from sqlite3 import Error
    from flask import jsonify

    def cursor_get(sql, database):
        try:
            db = sql.connect(database)
            cursor = db.cursor()
            cursor.execute(sql)
            registros = cursor.fetchall()
            if registros:
                nomes_colunas = [x[0] for x in cursor.description]

                json_dados = []
                for reg in registros:
                    json_dados.append(dict(zip(nomes_colunas, reg)))

                return jsonify(json_dados)
            else:
                return jsonify({'mensagem': 'Registro nao encontrado!'})
        except Error as e:
            return jsonify({'mensagem': e})
        finally:
            db.close()

    def cursor_post(sql, database):
        try:
            db = sql.connect(database)
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            return jsonify({'mensagem': 'Registro inserido com sucesso!'})
        except Error as e:
            return jsonify({'mensagem': e})
        finally:
            db.close()

    def cursor_delete(sql, database):
        try:
            db = sql.connect(database)
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            return jsonify({'mensagem': 'Registro excluido com sucesso!'})
        except Error as e:
            return jsonify({'mensagem': e})
        finally:
            db.close()