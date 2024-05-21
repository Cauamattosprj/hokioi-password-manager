import psycopg2
from time import sleep

def createUser():
    connection = psycopg2.connect(
        f"dbname=hokioidb user=postgres password=admin client_encoding=UTF8 port=5432"
        )
    
    # usuário irá inserir os dados da sua conta.
    username = input("Username: ")
    print(f'Seu nome de usuário: {username}')
    email = input("Email: ")
    password_try = input("Senha: ")
    password_confirm = input("Confime sua senha: ")

    while password_confirm != password_try:    
        if password_confirm == password_try:
            password_definitive = password_confirm
            return password_definitive
        else: 
            print('Senha de confirmação não confere com a senha informada. Tente novamente\n')
            password_try = input("Senha: ")
            password_confirm = input("Confime sua senha: ")

    # cursor irá colocar os valores no banco de dados.
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO users (username, email, password_hash) VALUES ({username}, {email}, {password_definitive})')


    cursor.close()
    connection.close()

def querySelector(query: str):
    connection = psycopg2.connect(
        f"dbname=hokioidb user=postgre password=admin client_encoding=UTF8 port=5432"
        )
    cursor = connection.cursor()
    
    cursor.execute(query)

    cursor.close()
    connection.close()