inventario = []

while True:
    accion = input("Ingresa una fruta: ").strip().lower()
    
    if accion == "salir":
        print("Programa finalizado.")
        break
        
    elif accion == "ver":
        print("Tu inventario:", inventario)  # ← Simple y funciona
        
    else:
        inventario.append(accion)
        print(f"Agregaste: {accion}")