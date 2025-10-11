# Ciberseguridad con Python
Proyecto Día 1: Script `verificar_usuario.py` que verifica el rol de un usuario (admin/usuario) para simular un control de acceso en ciberseguridad.



Notas del Día 1
- **Conceptos aprendidos**:
  - `input()`: Lee texto del usuario como cadena (`str`).
  - `print()`: Muestra mensajes en la terminal.
  - f-strings: Permiten insertar variables en texto (ej., `f"Acceso para {usuario}"`).
  - `lower()`: Convierte texto a minúsculas para normalizar entradas (p. ej., `"ADMIN"` → `"admin"`).
  - Expresión condicional: `'Autorizado' if rol.lower() == 'admin' else 'Restringido'` decide el mensaje en una línea.
- **Ciberseguridad**:
  - Este script simula un sistema de control de acceso, como los usados en servidores para verificar permisos de usuarios.
  - Validar entradas (`if not usuario`) es crucial para evitar procesar datos inválidos, lo que podría ser una vulnerabilidad.
- **Pruebas realizadas**:
  - `bryan/admin` → `Acceso para bryan: Autorizado`
  - `bryan/usuario` → `Acceso para bryan: Restringido`
- **Errores encontrados**:
  - Inicialmente, el mensaje se repetía por dos `print`. Corregido moviendo el `print` al bloque `else`.
- **Reflexión**:
  - Podría mejorar el script validando también el `rol` (p. ej., aceptar solo `"admin"` o `"usuario"`).


Día 2: Sistema de Acceso y Validación (11/10/2025)
- **Archivo**: `dia2_logica.py`
- **Descripción**: Programa que simula un sistema de acceso, validando nombre, contraseña y edad. Incluye un modo administrador especial.
- **Lo que aprendí**: 
  - Uso de condicionales `if-elif-else` para controlar el flujo del programa.
  - Operadores de comparación (`==`, `<`, `>=`) y lógicos (`and`).
  - Cómo usar `input()` para entradas de texto y `int()` para convertir a números.
- **Notas**: Resolví un error `TypeError: '>=' not supported between instances of 'str' and 'int'` al olvidar convertir la edad a entero. Aprendí a verificar tipos de datos antes de compararlos.






