if __name__ == "__main__":
    import sqlite3

    connection_obj = sqlite3.connect('db-livros.db')

    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("CREATE TABLE produtos (  \
        id      INTEGER PRIMARY KEY AUTOINCREMENT, \
        nome   TEXT, \
        quanitade	NUMERIC,   \
        editoraNTEGER, \
        vendedor_id INTEGER, \
        cliente_id	INTEGER, \
        valor	NUMERIC, \
        marca	TEXT, \
        modelo	TEXT, \
    );")
    connection_obj.commit()