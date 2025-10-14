
usuario = input("Ingresa tu alias : ")
rol = input("Ingresa tu rol (admin/usuario): ")
if not usuario:
    print("Error: Ingresa un alias.")
else:
    print(f"Acceso para {usuario}: {'Autorizado' if rol.lower() == 'admin' else 'Restringido'}")
