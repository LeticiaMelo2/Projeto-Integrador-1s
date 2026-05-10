from werkzeug.security import generate_password_hash, check_password_hash

senha = "123"
hash_gerado = generate_password_hash(senha)
print("Hash:", hash_gerado)
print("Confere:", check_password_hash(hash_gerado, senha))