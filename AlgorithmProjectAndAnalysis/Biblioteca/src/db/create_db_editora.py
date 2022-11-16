if __name__ == "__main__":
    import sqlite3

    connection_obj = sqlite3.connect('db-editora.db')

    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("CREATE TABLE editoras (  \
        id       INTEGER PRIMARY KEY AUTOINCREMENT, \
        cnpj     NUMERIC,   \
        nome     TEXT, \
        endereco TEXT, \
        numero   NUMERIC, \
        bairro   TEXT, \
        cidade   TEXT, \
        estado   TEXT, \
        cep      NUMERIC, \
        telefone NUMERIC, \
        email    TEXT \
    );")
    connection_obj.commit()