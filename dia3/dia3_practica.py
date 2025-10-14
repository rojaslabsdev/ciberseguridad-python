
##VALIDACION LOGIN CODIGO
usuario_correcto = "bryan"
password_correcto = "1234"

while True:
    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    if usuario == usuario_correcto and password == password_correcto:
        print("✅ Bienvenido,", usuario)
        break
    else:
        print("❌ Datos incorrectos, intenta de nuevo.")

