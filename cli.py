def newAccount():
    username = input("Username: ")
    password_try = input("Password: ")
    password_confirm = input("Confirm your password: ")

    







print("**********************************")
print("Welcome to Hokioi Password Manager")
print("**********************************")

# Criar conta ou logar em conta
decision = input("1 - Login \n2 - New Account")

if decision == 1:
    login()
elif decision == 2:
    newAccount()


# Menu interativo 

# Cadastrar novos logins e senhas