"""
Ejercicio 4 — Captura de ValidationError

Escribir un bloque de código que intente instanciar un modelo `UsuarioSistema`
con campos:

- `email`: utilizar `EmailStr`.
- `nivel_acceso`: entero entre 1 y 5.

Proveyendo datos incorrectos. Capturar explícitamente la excepción
`ValidationError` imprimiendo por pantalla los errores detallados.
(Ver: `try/except`)
"""

from pydantic import BaseModel, EmailStr, Field, ValidationError


class UsuarioSistema(BaseModel):
    """Modelo de un usuario del sistema."""

    email: EmailStr
    nivel_acceso: int = Field(ge=1, le=5)


def main():
    # Instancia válida
    usuario_valido = UsuarioSistema(
        email="pepito@unemail.com",
        nivel_acceso=3,
    )
    print("Instancia válida:")
    print(usuario_valido)
    print()

    # Datos incorrectos: email inválido y nivel_acceso fuera de rango
    print("Error: datos incorrectos")
    try:
        usuario_no_valido = UsuarioSistema(
            email="no-es-un-email",
            nivel_acceso=9,
        )
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()