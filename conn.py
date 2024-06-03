import psycopg2

def login():
    connection = psycopg2.connect(
        "dbname=hokioidb user=postgres password=ADMIN client_encoding=UTF8 port=5432"
    )
    cursor = connection.cursor()

    user_id = None

    while True:
        username_input = str(input("LOGIN: "))
        password_input = input("SENHA: ")

        try:
            cursor.execute(
                "SELECT id, username, password_hash FROM users WHERE username = %s AND password_hash = %s;",
                (username_input, password_input)
            )
            login_return = cursor.fetchone()
            print(login_return)

            if login_return:
                user_id = login_return[0]
                print(f"LOGIN BEM SUCEDIDO!")
                break  
            else:
                print("USUÁRIO NÃO ENCONTRADO. Tente novamente.")
        except Exception as e:
            print(f"Erro ao acessar o banco de dados: {e}")

    # Fechar a conexão com o banco de dados
    cursor.close()
    connection.close()

    if user_id:
        manage_accounts(user_id)

def manage_accounts(user_id):
    while True:
        print("\nMENU")
        print("1. Ver contas")
        print("2. Criar nova conta")
        print("3. Exluir Contas")
        print("4. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            view_accounts(user_id)
        elif choice == '2':
            create_account(user_id)
        elif choice == '3':
            exclude_accounts(user_id)
        elif choice == '4':
            break
        else:
            print("Opção inválida, tente novamente.")
        

def view_accounts(user_id):
    connection = psycopg2.connect(
        "dbname=hokioidb user=postgres password=ADMIN client_encoding=UTF8 port=5432"
    )
    cursor = connection.cursor()
    try:
        cursor.execute(
            "SELECT id, account_name, username, password, website_url, created_at FROM accounts WHERE user_id = %s;",
            (user_id,)
        )
        
        col_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        
        print(", ".join(col_names))
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
    finally:
        cursor.close()
        connection.close()

def create_account(user_id):
    connection = psycopg2.connect(
        "dbname=hokioidb user=postgres password=ADMIN client_encoding=UTF8 port=5432"
    )

    account_name = input("Nome da Conta: ")
    username = input("Nome de Usuário: ")
    password = input("Senha: ")
    website_url = input("URL do Site: ")

    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO accounts (account_name, username, password, website_url, created_at, user_id) VALUES (%s, %s, %s, %s, NOW(), %s)",
            (account_name, username, password, website_url, user_id)
        )
        connection.commit()
        print("Conta criada com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir no banco de dados: {e}")
    finally:
        cursor.close()
        connection.close()

def exclude_accounts(user_id):
    connection = psycopg2.connect(
        "dbname=hokioidb user=postgres password=ADMIN client_encoding=UTF8 port=5432"
    )
    cursor = connection.cursor()
    cursor.execute('SELECT account_name FROM accounts WHERE user_id = %s;', user_id)
    account_excluded = ("Escolha a conta que você deseja excluir: ")

    try:
        cursor.execute('DELETE FROM accounts WHERE account_name = %s', account_excluded)
        print(f"Conta excluída com sucesso! ({account_excluded})")
    except Exception as e:
        print(f"Erro ao realizar a exclusão: {e}")
    finally:
        cursor.close()
        connection.close()


def createUser():
    connection = psycopg2.connect(
        "dbname=hokioidb user=postgres password=ADMIN client_encoding=UTF8 port=5432"
    )

    username = input("Username: ")
    print(f'Seu nome de usuário: {username}')
    email = input("Email: ")
    password_try = input("Senha: ")
    
    while True:
        password_confirm = input("Confirme sua senha: ")
        if password_confirm == password_try:
            break
        else:
            print('Senha de confirmação não confere com a senha informada. Tente novamente\n')

    password_definitive = password_try

    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, password_definitive)
        )
        connection.commit()
        print("Usuário criado com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir no banco de dados: {e}")
    finally:
        cursor.close()
        connection.close()


def createUser():
    connection = psycopg2.connect(
        "dbname=hokioidb user=postgres password=ADMIN client_encoding=UTF8 port=5432"
    )

    username = input("Username: ")
    print(f'Seu nome de usuário: {username}')
    email = input("Email: ")
    password_try = input("Senha: ")
    
    while True:
        password_confirm = input("Confirme sua senha: ")
        if password_confirm == password_try:
            break
        else:
            print('Senha de confirmação não confere com a senha informada. Tente novamente\n')

    password_definitive = password_try

    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, password_definitive)
        )
        connection.commit()
        print("Usuário criado com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir no banco de dados: {e}")
    finally:
        cursor.close()
        connection.close()

def querySelector(query: str):
    connection = psycopg2.connect(
        "dbname=hokioidb user=postgres password=ADMIN client_encoding=UTF8 port=5432"
    )
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        
        col_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        
        print(", ".join(col_names))
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
    finally:
        cursor.close()
        connection.close()
