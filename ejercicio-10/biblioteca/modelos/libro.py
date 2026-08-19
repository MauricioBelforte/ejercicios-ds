"""
Ejercicio 10 — Esquema de archivos (biblioteca)
Parte 1 — libro.py

En `libro.py`, definir la clase `Libro`. Añadir más atributos si lo cree necesario.
"""


class Libro:
    """Representa un libro en la biblioteca."""

    def __init__(self, titulo, autor, isbn, disponible = True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def __str__(self):
        if self.disponible:
            estado = "Disponible"
        else:
            estado = "Prestado"
        return f"'{self.titulo}' de {self.autor} ({self.isbn}) - {estado}"