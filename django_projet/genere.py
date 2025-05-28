import bcrypt
password = b"Hitema2025"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed.decode())