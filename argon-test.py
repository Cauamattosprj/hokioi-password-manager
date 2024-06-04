import argon2

ph = argon2.PasswordHasher()

senha = input("Digite sua senha segura: ")

hash = ph.hash(senha)

print(hash)

print(ph.verify(hash, "Peita"))
print(ph.check_needs_rehash(hash))