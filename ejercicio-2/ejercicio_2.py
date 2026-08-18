"""
Ejercicio 2 — ¡Hola <arg 1>!

Modifique el programa anterior para que muestre "¡Hola <arg 1>!", donde `arg 1`
proviene de la lista de argumentos al ejecutar el programa.

- Ejemplo: al ejecutar `python ejercicio_2.py firulais`, el programa mostrará "¡Hola Firulais!".
- Utilice métodos de string para "capitalizar" el argumento recibido por parámetros.
"""

import sys



def main():
    nombre = sys.argv[1]
    print(f"¡Hola {nombre.capitalize()}!")


if __name__ == "__main__":
    main()