if __name__ == "__main__":
    import sqlite3

    connection_obj = sqlite3.connect('db-cliente.db')

    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("CREATE TABLE clientes (  \
        id              INTEGER PRIMARY KEY AUTOINCREMENT, \
        email           TEXT, \
        nome	        TEXT,   \
        cpf	            NUMERIC, \
        telefone        NUMERIC, \
        sexo	        CHARACTER(1), \
        data_nascimento	DATE, \
        cep	            NUMERIC, \
        endereco	    TEXT, \
        numero	        NUMERIC, \
        bairro	        TEXT \
    );")
    connection_obj.commit()