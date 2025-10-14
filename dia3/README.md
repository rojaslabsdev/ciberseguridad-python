Notas Día 3 – Bucles for y while

Qué es un bucle:
Un bucle permite repetir una acción varias veces sin tener que escribir el mismo código. Sirven para automatizar tareas repetitivas o recorrer listas, textos, etc.

Bucle for:
Se usa cuando sabemos cuántas veces queremos repetir algo.
Sintaxis:
for variable in rango:
acción a repetir

Ejemplo:
for i in range(5):
print("Repetición número:", i)

Esto imprimirá del 0 al 4 (5 repeticiones en total).

Notas:

* range(5) genera una secuencia del 0 al 4
* Puedes personalizar el inicio y fin: range(1, 6) → del 1 al 5
* Puedes agregar un salto: range(0, 10, 2) → 0, 2, 4, 6, 8
* Muy útil para recorrer listas:
  nombres = ["Ana", "Luis", "Bryan"]
  for nombre in nombres:
  print("Hola", nombre)

Bucle while:
Se usa cuando no sabemos cuántas veces se repetirá una acción, pero tenemos una condición lógica que debe cumplirse para continuar.
Sintaxis:
while condición:
acción a repetir

Ejemplo:
contador = 0
while contador < 5:
print("Contador:", contador)
contador += 1

Repite mientras la condición sea verdadera (contador < 5).

Notas:

* Si la condición nunca cambia a False, el bucle será infinito
* Puedes usar break para detener el ciclo y continue para saltar una vuelta

Diferencias clave:
for → repite un número fijo de veces, ideal para recorrer listas o rangos, más estructurado.
while → repite mientras se cumpla una condición, ideal para validaciones o menús interactivos, más flexible.
