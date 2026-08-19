"""
Ejercicio 10 — Esquema de archivos (biblioteca)
Parte 3 — main.py

Finalmente, crear un archivo principal `main.py` **fuera** de la carpeta `biblioteca` que:
- Importe las funcionalidades usando la organización de espacios de nombres, p. ej.:
  ```python
  from biblioteca.modelos.libro import Libro
  ```
- Ejecute un caso de uso invocando a **todos los métodos** del módulo `prestamo.py`.
"""

from biblioteca.modelos.libro import Libro
from biblioteca.servicios.prestamo import (
    consultar_disponibilidad,
    realizar_devolucion,
    realizar_prestamo,
)


def main():
    # Crear un libro
    libro = Libro("Cien años de soledad", "Gabriel García Márquez",4543)

    # Consultar disponibilidad inicial
    print(consultar_disponibilidad(libro))

    # Realizar préstamo
    print(realizar_prestamo(libro))
    print(consultar_disponibilidad(libro))

    # Intentar prestar de nuevo (debería fallar)
    print(realizar_prestamo(libro))

    # Realizar devolución
    print(realizar_devolucion(libro))
    print(consultar_disponibilidad(libro))

    # Intentar devolver de nuevo (debería fallar)
    print(realizar_devolucion(libro))


if __name__ == "__main__":
    main()