"""
Ejercicio 10 — Esquema de archivos (biblioteca)
Parte 2 — prestamo.py

En `prestamo.py`, importar la clase `Libro` utilizando **rutas relativas o absolutas
correctas** dentro del paquete e implementar un par de operaciones. Implementar las
funciones para:

- **Realizar préstamo**
- **Realizar devolución**
- **Consultar disponibilidad**

#### Realizar préstamo:
- Recibir un objeto `Libro` por parámetros.
- Verificar si `libro.disponible` es `True`.
  - Si lo está, cambiar su estado a `False` y retornar un **mensaje de éxito**.
  - Si ya está prestado, informar que **no se encuentra disponible**.

#### Realizar devolución:
- Recibir un objeto `Libro`.
- Verificar si el libro estaba prestado (`disponible == False`).
  - Si es así, cambiar su estado a `True` y retornar un **mensaje de éxito**.
  - De lo contrario, indicar que el libro **ya figuraba como disponible** en la biblioteca.

#### Consultar disponibilidad:
- Recibir `Libro` y retornar su estado actual de forma **amigable**.
"""

from biblioteca.modelos.libro import Libro


def realizar_prestamo(libro):
    """Realiza un préstamo si el libro está disponible."""
    if libro.disponible:
        libro.disponible = False
        return f"Préstamo exitoso: {libro.titulo}."
    return f"El libro '{libro.titulo}' no se encuentra disponible."


def realizar_devolucion(libro):
    """Realiza una devolución si el libro estaba prestado."""
    if not libro.disponible:
        libro.disponible = True
        return f"Devolución exitosa: {libro.titulo}."
    return f"El libro '{libro.titulo}' ya figuraba como disponible en la biblioteca."


def consultar_disponibilidad(libro):
    """Retorna el estado actual del libro de forma amigable."""
    if libro.disponible:
        estado = "disponible"
    else:
        estado = "prestado"
    return f"El libro '{libro.titulo}' se encuentra {estado}."