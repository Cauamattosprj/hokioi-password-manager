import psycopg2

def createUser():
    connection = psycopg2.connect(
        f"dbname=hokioidb user=postgres password=ADMIN client_encoding=UTF8 port=5432"
    )

    # Usuário irá inserir os dados da sua conta.
    username = input("Username: ")
    print(f'Seu nome de usuário: {username}')
    email = input("Email: ")
    password_try = input("Senha: ")
    
    # Loop enquanto a senha de confirmação não coincidir com a senha informada.
    while True:
        password_confirm = input("Confime sua senha: ")
        if password_confirm == password_try:
            break
        else:
            print('Senha de confirmação não confere com a senha informada. Tente novamente\n')

    # Após o loop, a senha correta está armazenada em password_try.
    password_definitive = password_try

    # Cursor irá colocar os valores no banco de dados.
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)', (username, email, password_definitive))
    
    connection.commit()  # Confirmar as alterações no banco de dados.
    cursor.close()
    connection.close()




    

def querySelector(query: str):
    connection = psycopg2.connect(
        f"dbname=hokioidb user=postgres password=ADMIN client_encoding=UTF8 port=5432"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    
    # Obtendo os nomes das colunas do cursor
    col_names = [desc[0] for desc in cursor.description]

    # Recuperando os resultados da consulta
    rows = cursor.fetchall()

    # Imprimindo os nomes das colunas
    print(", ".join(col_names))

    # Imprimindo os resultados da consulta
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
