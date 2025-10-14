Notas Día 4 – Listas y Tuplas

Hoy aprendí a trabajar con estructuras de datos básicas en Python: listas y tuplas.

Una lista es una colección de elementos ordenados y modificables. Se crean con corchetes [].
Ejemplo: frutas = ["manzana", "plátano", "naranja"]

Puedo acceder a los elementos por su índice, modificar valores, agregar o eliminar elementos.
Ejemplos:
frutas.append("uva") → agrega un nuevo elemento
frutas.remove("plátano") → elimina un elemento
frutas[0] = "pera" → cambia el valor del primer elemento
len(frutas) → devuelve la cantidad de elementos

También aprendí que puedo recorrer una lista con un for:
for fruta in frutas:
print(fruta)

Las tuplas son parecidas a las listas, pero no se pueden modificar (son inmutables).
Se crean con paréntesis ():
colores = ("rojo", "verde", "azul")

Diferencias principales:
Las listas son mutables y usan corchetes [].
Las tuplas son inmutables y usan paréntesis ().

Proyecto del día: “Gestor simple de frutas”
Aprendí a crear una lista vacía (inventario = []) y a usar un ciclo while con condicionales.
El programa pide al usuario que ingrese frutas, permite ver el inventario o salir del programa.
