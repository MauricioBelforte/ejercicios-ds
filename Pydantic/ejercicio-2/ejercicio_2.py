"""
Ejercicio 2 — Modelo Dispositivo

Crear un modelo `Dispositivo` que contenga:

- `id_dispositivo`: puede ser un entero o una cadena.
- `tipo`: `Literal` que solo acepte los valores "sensor", "actuador" o "gateway".

Crear una instancia de este modelo para comprobar el uso del atributo
`id_dispositivo` como `Union` de dos tipos de datos y otra instancia para
comprobar el error de validación al utilizar valores inválidos.
"""

from typing import Literal, Union

from pydantic import BaseModel, ValidationError


class Dispositivo(BaseModel):
    """Modelo de un dispositivo."""

    id_dispositivo: Union[int, str]
    tipo: Literal["sensor", "actuador", "gateway"]


def main():
    # Instancia válida con id_dispositivo entero
    dispositivo_1 = Dispositivo(id_dispositivo=101, tipo="sensor")
    print("Dispositivo con id entero:")
    print(dispositivo_1)
    print()

    # Instancia válida con id_dispositivo string
    dispositivo_2 = Dispositivo(id_dispositivo="SENSOR-101", tipo="actuador")
    print("Dispositivo con id string:")
    print(dispositivo_2)
    print()

    # Instancia inválida: tipo no permitido
    print("Error: tipo inválido")
    try:
        Dispositivo(id_dispositivo=102, tipo="pulsador")
    except ValidationError as e:
        print(e)
    print()

    # Instancia inválida: id_dispositivo con tipo no soportado
    print("Error: id_dispositivo inválido")
    try:
        Dispositivo(id_dispositivo=10.5, tipo="gateway")
    except ValidationError as e:
            print(e)

if __name__ == "__main__":
    main()