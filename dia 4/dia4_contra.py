# Lista de contraseñas débiles conocidas
contrasenas_debiles = []

print("DETECTOR DE CONTRASEÑAS DÉBILES")
print("Comandos: agregar/ver/verificar/salir")

while True:
    accion = input("Ingresa comando: ").strip().lower()
    
    if accion == "salir":
        print(" Análisis finalizado.")
        break
        
    elif accion == "ver":
        print("Contraseñas débiles conocidas:", contrasenas_debiles)
        
    elif accion == "verificar":
        # Pedir contraseña a verificar
        password = input("Ingresa contraseña a verificar: ").strip()
        if password in contrasenas_debiles:
            print(f" ¡PELIGRO! '{password}' está en lista negra")
        else:
            print(f" '{password}' no está en nuestra lista (aún...)")
            
    else:
        # AGREGAR como contraseña débil
        contrasenas_debiles.append(accion)
        print(f" Agregaste '{accion}' como contraseña débil")