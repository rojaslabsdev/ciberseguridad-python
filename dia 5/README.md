Notas Día 5 – Diccionarios y Conjuntos

Hoy aprendí a trabajar con diccionarios y conjuntos en Python.

Diccionario: estructura de datos que almacena pares clave:valor.
Ejemplo: usuario = {"nombre": "bryan", "edad": "24"}

Puedo acceder a un valor con la clave: usuario["nombre"] → bryan
Puedo agregar o modificar datos: usuario["pais"] = "México"
Puedo eliminar claves: del usuario["edad"]

También aprendí a recorrer un diccionario:
for clave, valor in usuario.items():
print(clave, ":", valor)

Conjuntos: colección de elementos únicos, no ordenada.
Ejemplo: frutas = {"manzana", "pera", "uva"}

Se eliminan duplicados automáticamente.

Operaciones útiles: add(), remove(), unión (|), intersección (&), diferencia (-).

Proyecto del día: Gestor de usuarios

Permite agregar, ver y buscar usuarios con su edad usando un diccionario.

Usa un bucle while con condicionales para el menú.

Lo más importante fue entender cómo actualizar el diccionario con un nuevo usuario y cómo buscar usando condicionales.
