"""
Ejercicio 1 — Modelo Estudiante

Crear un modelo `Estudiante` que contenga:

- `legajo`: entero positivo.
- `nombre_completo`: string de al menos 5 caracteres.
- `email`: string con formato de correo electrónico.
- `promedio`: float entre `0.0` y `10.0` con valor por defecto de `0.0`.

Crear una instancia por cada posible error de validación para observar el
mensaje que nos da Python al utilizar valores inválidos.
"""

from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing import Annotated

class Estudiante(BaseModel):
    """Modelo de un estudiante."""

    legajo: Annotated[int, Field(gt=0, description="Entero positivo")]
    nombre_completo: str = Field(min_length=5, description="Al menos 5 caracteres")
    email: EmailStr = Field(description="Formato de correo electrónico")
    promedio: float = Field(default=0.0, ge=0.0, le=10.0, description="Float entre 0.0 y 10.0")


def main():
    # Instancia válida
    estudiante_valido = Estudiante(
        legajo=12345,
        nombre_completo="María Pérez",
        email="maria.perez@example.com",
        promedio=8.5,
    )
    print("Instancia válida:")
    print(estudiante_valido)
    print()

    # 1. Error en Legajo (número negativo)
    print("ERROR 1: Legajo inválido")
    try:
        Estudiante(
            legajo=-5,
            nombre_completo="Juan Pérez",
            email="juan@ejemplo.com"
        )
    except ValidationError as e:
        print(e)
    print()

    # 2. Error en Nombre Completo (menos de 5 caracteres)
    print("ERROR 2: Nombre corto")
    try:
        Estudiante(
            legajo=10,
            nombre_completo="Ana",
            email="ana@ejemplo.com"
        )
    except ValidationError as e:
        print(e)
    print()

    # 3. Error en Email (formato incorrecto)
    print("ERROR 3: Email inválido")
    try:
        Estudiante(
            legajo=10,
            nombre_completo="Carlos Gómez",
            email="correo-sin-arroba.com"
        )
    except ValidationError as e:
        print(e)
    print()

    # 4. Error en Promedio (mayor a 10.0)
    print("ERROR 4: Promedio fuera de rango")
    try:
        Estudiante(
            legajo=10,
            nombre_completo="María López",
            email="maria@ejemplo.com",
            promedio=11.5
        )
    except ValidationError as e:
        print(e)

if __name__ == "__main__":
    main()