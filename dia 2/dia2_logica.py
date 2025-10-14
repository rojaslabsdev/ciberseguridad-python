# Sistema simple de acceso y validación

# Pedir datos al usuario
nombre = input("¿Cuál es tu nombre? ")
contrasena = input("¿Cuál es la contraseña? ")
edad = int(input("¿Cuál es tu edad? "))
#int(input) para convertir str a int permitir mas bien
# Validaciones
if nombre == "admin" and contrasena == "root123":
    print("Acceso total (modo administrador).")
elif edad < 18:
    print("Acceso denegado por edad.")
elif contrasena == "minion123":
    print("Bienvenido", nombre, ", acceso concedido.")
else:
    print("Contraseña incorrecta.")