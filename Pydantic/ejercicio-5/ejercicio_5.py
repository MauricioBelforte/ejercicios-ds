"""
Ejercicio 5 — Modelo PerfilUsuario

Construir un modelo `PerfilUsuario` que combine:

- `username`: string alfanumérico en minúsculas usando el atributo `pattern`
  de `Field` y la expresión regular `r"^[a-z0-9_]{3,20}$"`.
- `biografia`: opcional, con un máximo de 200 caracteres.
- `redes_sociales`: lista opcional de strings, URLs o nombres. (Ver `Types/urls`)
"""

from typing import Annotated, Optional, Union
from pydantic import BaseModel, Field, HttpUrl, ValidationError


class PerfilUsuario(BaseModel):
    """Modelo de perfil de usuario con validaciones de Regex (Expresiones Regulares), longitud y URLs."""

    username: Annotated[str,Field(pattern=r"^[a-z0-9_]{3,20}$",description="String alfanumérico en minúsculas entre 3 y 20 caracteres")]
    
    biografia: Optional[str] = Field(default=None,max_length=200,description="Texto opcional de hasta 200 caracteres")
    
    # Acepta una lista que contenga objetos HttpUrl o cadenas de texto simples (ej: "@mi_usuario")
    redes_sociales: Optional[list[Union[HttpUrl, str]]] = Field(default=None,description="Lista opcional de URLs o nombres de redes sociales")


def main():
    print("INSTANCIAS VÁLIDAS")

    # 1. Perfil completo con todos los campos válidos
    perfil_completo = PerfilUsuario(
        username="maurybelfort",
        biografia="Desarrollador de software y entusiasta de la tecnología.",
        redes_sociales=["https://github.com/mauriciobelforte", "https://instagram.com/maury"],
    )
    print("Perfil completo:")
    print(perfil_completo)
    print()

    # 2. Perfil solo con username, dejando los opcionales en None
    perfil_minimo = PerfilUsuario(username="usuario123")
    print("Perfil mínimo (con opcionales por defecto):")
    print(perfil_minimo)
    print()

    print("INSTANCIAS CON ERROR DE VALIDACIÓN")

    # 3. Error en 'username': Mayúsculas y caracteres no permitidos
    print("ERROR 1: Username con mayúsculas o caracteres especiales no permitidos")
    try:
        PerfilUsuario(username="Usuario-Invalido!")
    except ValidationError as e:
        print(e)
    print()

    # 4. Error en 'username': Menos de 3 caracteres
    print("ERROR 2: Username demasiado corto")
    try:
        PerfilUsuario(username="al")
    except ValidationError as e:
        print(e)
    print()

    # 5. Error en 'biografia': Más de 200 caracteres
    print("ERROR 3: Biografía demasiado larga")
    try:
        PerfilUsuario(
            username="bio_test",
            biografia="A" * 205  # Genera una cadena de 205 caracteres 'A'
        )
    except ValidationError as e:
        print(e)



if __name__ == "__main__":
    main()