"""
Ejercicio 3 — Tipo reutilizable CoordenadaGPS

Crear un tipo reutilizable `CoordenadaGPS` con `Annotated` que sea un `float`
entre `-90.0` y `90.0`.

Luego, implementa un modelo `Ubicacion` que use este tipo de dato para sus
atributos: `longitud` y `latitud` y que además tenga un atributo opcional
`etiqueta` (string).

- Crear una instancia de este modelo para comprobar el uso del tipo
  reutilizable, mostrando por pantalla lo que tenga la instancia.
- Crear otra instancia para comprobar el error de validación al utilizar
  valores inválidos de latitud/longitud.
"""

from typing import Annotated, Optional

from pydantic import BaseModel, Field, ValidationError

# Tipo reutilizable: float entre -90.0 y 90.0
CoordenadaGPS = Annotated[float, Field(ge=-90.0, le=90.0)]


class Ubicacion(BaseModel):
    """Modelo de una ubicación geográfica."""

    longitud: CoordenadaGPS
    latitud: CoordenadaGPS
    etiqueta: Optional[str] = None


def main():
    # Instancia válida
    ubicacion_valida = Ubicacion(
        longitud=-58.4,
        latitud=-34.6,
        etiqueta="Buenos Aires",
    )
    print("Instancia válida:")
    print(ubicacion_valida)
    print()

    # Instancia inválida: latitud fuera de rango
    print("Error: latitud fuera de rango")
    try:
        Ubicacion(longitud=10.0, latitud=95.0)
    except ValidationError as e:
        print(e)
    print()

    # Instancia inválida: longitud fuera de rango
    print("Error: longitud fuera de rango")
    try:
        Ubicacion(longitud=-100.0, latitud=45.0)
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()