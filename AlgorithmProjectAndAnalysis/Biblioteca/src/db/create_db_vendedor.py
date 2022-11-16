if __name__ == "__main__":
    import sqlite3

    connection_obj = sqlite3.connect('db-vendedor.db')

    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("CREATE TABLE vendedores (  \
        id              INTEGER PRIMARY KEY AUTOINCREMENT, \
        email           TEXT, \
        nome	        TEXT,   \
        cpf_cnpj	    NUMERIC NULL, \
        telefone        NUMERIC, \
        sexo	        CHARACTER(1) NULL, \
        data_nascimento	DATE, \
        cep	            NUMERIC, \
        endereco 	    TEXT, \
        numero	        NUMERIC, \
        bairro	        TEXT \
    );")
    connection_obj.commit()