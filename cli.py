from conn import *

print("**********************************")
print("Welcome to Hokioi Password Manager")
print("**********************************")

# Criar conta ou logar em conta
decision = input("1 - Login \n2 - New Account\n")

while True:
    if decision == "1":
        print("DECISÃO 1")        
        print("USUÁRIOS: ")
        querySelector('SELECT username FROM users;')
        login()
    elif decision == "2":
        print("DECISAO 2")
        createUser()

# Menu interativo 

# Cadastrar novos logins e senhas