user = "admin@admin.co"
password = "1234"

user_input = input("Ingrese el usuario: ")
password_input = input("Ingrese contraseña: ")

if user_input == user and password_input == password:
    input("Sesion inciada paulatinamente")
else:
    input("usuario o contraseña incorrecta")
