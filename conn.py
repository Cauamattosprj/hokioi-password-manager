import psycopg2
import argon2
from time import sleep

ph = argon2.PasswordHasher()

def hashPass(password):
    hashed_password = ph.hash(password)
    return hashed_password

def createUser():
    connection = psycopg2.connect(
        "dbname=hokioidb user=postgres password=ADMIN client_encoding=UTF8 port=5432"
    )

    username = input("Username: ")
    print(f'Seu nome de usuário: {username}')
    email = input("Email: ")
    
    while True:
        password_try = input("Senha: ")
        password_confirm = input("Confirme sua senha: ")
        if password_confirm == password_try:
            break
        else:
            print('Senha de confirmação não confere com a senha informada. Tente novamente\n')
    definitive_password = password_try
    hashed_password = hashPass(definitive_password)

    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, hashed_password)
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

def login():
    connection = psycopg2.connect(
        "dbname=hokioidb user=postgres password=ADMIN client_encoding=UTF8 port=5432"
    )
    cursor = connection.cursor()

    user_id = None

    while True:
        username_input = str(input("LOGIN: "))
        password_input = input("SENHA: ")

        # Vai no db retornar o password_hash do usuário buscado
        cursor.execute("SELECT id, password_hash FROM users WHERE username = %s", (username_input,))
        result = cursor.fetchone()

        if result:
            user_id, hashed_db_password = result

            try:
                # Verificar se a senha está correta
                ph.verify(hashed_db_password, password_input)

                # Se a senha for verificada, podemos verificar se o hash precisa ser atualizado
                if ph.check_needs_rehash(hashed_db_password):
                    new_hashed_password = hashPass(password_input)
                    cursor.execute(
                        "UPDATE users SET password_hash = %s WHERE id = %s",
                        (new_hashed_password, user_id)
                    )
                    connection.commit()

                print("LOGIN BEM SUCEDIDO!")
                break

            except argon2.exceptions.VerifyMismatchError:
                print("SENHA INCORRETA. Tente novamente.")
        else:
            print("USUÁRIO NÃO ENCONTRADO. Tente novamente.")

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
        print("3. Excluir Contas")
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
            "SELECT account_name, username, password FROM accounts WHERE user_id = %s;",
            (user_id,)
        )
        
        results = cursor.fetchall()

        for i, row in enumerate(results):
            print(f"Nome da conta: {row[0]}\nLogin: {row[1]}\nSenha: ***** (Para revelar digite: {i})")
            print("-------------")

        choice = input("1. Revelar senhas")
        if choice == "1":
            choice = input("Digite o número da conta na qual você deseja revelar a senha: ")
            reveal_password = choice
            cursor.execute("SELECT password FROM accounts WHERE user_id = %s;", (user_id,)) 
            password_hash = cursor.fetchall()
            print(f"SENHA HASH PARA SER REVELADA: {password_hash[0]}")
            # REVELAR A SENHA PARA O USUÁRIO


    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
    finally:
        cursor.close()
        connection.close()

def reveal_password(user_id, ):
    # Conecta banco
    connection = psycopg2.connect(
        "dbname=hokioidb user=postgres password=ADMIN client_encoding=UTF8 port=5432"
    )
    cursor = connection.cursor()


    # pergunta qual conta
    choice = input("Qual conta você deseja a senha? ")
    

    # faz querie pela conta selecionada retornando o password_hash
    # desfaz o hash para texto plano



def create_account(user_id):
    connection = psycopg2.connect(
        "dbname=hokioidb user=postgres password=ADMIN client_encoding=UTF8 port=5432"
    )

    account_name = input("Nome da Conta: ")
    username = input("Nome de Usuário: ")
    while True:
        password = input("Senha: ")
        password_try = input("Confirme sua senha: ")
        if password_try == password:
            break
        else: 
            print("Senhas não coincidem. Tente novamente.")
    hashed_password = hashPass(password)
    website_url = input("URL do Site: ")

    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO accounts (account_name, username, password, website_url, created_at, user_id) VALUES (%s, %s, %s, %s, NOW(), %s)",
            (account_name, username, hashed_password, website_url, user_id)
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
    try:
        cursor.execute('SELECT account_name FROM accounts WHERE user_id = %s;', (user_id,))
        accounts = cursor.fetchall()

        if not accounts:
            print("Nenhuma conta encontrada para exclusão.")
            return

        print("Contas disponíveis para exclusão:")
        for idx, account in enumerate(accounts, 1):
            print(f"{idx}. {account[0]}")

        choice = int(input("Escolha a conta que você deseja excluir (número): "))
        account_to_delete = accounts[choice - 1][0]

        cursor.execute('DELETE FROM accounts WHERE account_name = %s AND user_id = %s', (account_to_delete, user_id))
        connection.commit()
        print(f"Conta excluída com sucesso: {account_to_delete}")

    except Exception as e:
        print(f"Erro ao realizar a exclusão: {e}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    print("**********************************")
    print("Welcome to Hokioi Password Manager")
    print("**********************************")
    print("1 - Login")
    print("2 - New Account")

    decision = input()
    print(f"DECISÃO {decision}")
    
    if decision == "1":
        login()
    elif decision == "2":
        createUser()
    else:
        print("Opção inválida.")
