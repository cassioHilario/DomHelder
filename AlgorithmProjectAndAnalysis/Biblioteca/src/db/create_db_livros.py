if __name__ == "__main__":
    import sqlite3

    connection_obj = sqlite3.connect('db-livro.db')

    cursor_obj = connection_obj.cursor()
    
    # Tabela backup clientes
    cursor_obj.execute("CREATE TABLE clientes (  \
        id              INTEGER, \
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
    
    # Tabela backup vendedores
    cursor_obj.execute("CREATE TABLE vendedores (  \
        id              INTEGER, \
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
    
    # Tabela backup editoras
    cursor_obj.execute("CREATE TABLE editoras (  \
        id       INTEGER, \
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

    cursor_obj.execute("CREATE TABLE livros (  \
        id          INTEGER PRIMARY KEY AUTOINCREMENT, \
        nome        TEXT, \
        quantidade	NUMERIC, \
        vendedor_id INTEGER, \
        cliente_id	INTEGER, \
        editora_id	INTEGER, \
        valor	    NUMERIC, \
        edicao	    TEXT, \
        foreign key (vendedor_id) references vendedores(id), \
        foreign key (cliente_id) references clientes(id), \
        foreign key (editora_id) references editoras(id) \
    );")
    connection_obj.commit()    
    connection_obj.close()