usuario = {
"nombre" : "bryan",
"edad" : "24"
}

while True:
    accion = input("Desea agregar usuario , ver , buscar o salir: ")
    if accion == "salir":
        print("Hasta luego.")
        break
    elif accion == "ver": 
        print(f"Estos son los usuarios: {usuario['nombre']}. Edad: {usuario['edad']}")
    elif accion == "buscar":
        nombre_buscar = input("Ingrese el nombre a buscar : ")
        if nombre_buscar.lower() == usuario['nombre'].lower():
            print(f"Encontrado , {usuario['nombre']}, Edad: {usuario['edad']}")
        else:
            print("usuario no encontrado")
    elif accion == "agregar":
        nuevo_nombre = input("Que nombre desea agregar: ")        
        nueva_edad = input("Que edad tiene?: ")   
        usuario = { 
            "nombre" : nuevo_nombre,
            "edad" : nueva_edad
        }
        print(f"Usuario actualizado: {nuevo_nombre}, {nueva_edad}")
    else: 
        print("opcion no valida ingrese una valida")



   


