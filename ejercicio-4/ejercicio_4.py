"""
Ejercicio 4 — Conversión de temperatura

Escriba un programa que permita hacer la conversión de valores de temperatura entre
**Celsius** y **Fahrenheit**.

- Solicitar al usuario que ingrese un **valor numérico** y la **escala original**.
- Mostrar por pantalla el valor convertido incluyendo la **escala final**.
- Construir **dos funciones**:
  - Una para convertir datos a escala **Celsius**.
  - Otra para convertir datos a escala **Fahrenheit**.

> Ver `input()`.
"""


def celsius_a_fahrenheit(valor):
    """Convierte un valor de Celsius a Fahrenheit."""
    return (valor * 9 / 5) + 32


def fahrenheit_a_celsius(valor):
    """Convierte un valor de Fahrenheit a Celsius."""
    return (valor - 32) * 5 / 9


def main():
    valor = float(input("Ingrese el valor numérico de la temperatura: "))
    escala = input("Ingrese la escala original (C para Celsius, F para Fahrenheit): ").strip().upper()

    if escala == "C":
        resultado = celsius_a_fahrenheit(valor)
        print(f"{valor} °C equivalen a {resultado} °F")
    elif escala == "F":
        resultado = fahrenheit_a_celsius(valor)
        print(f"{valor} °F equivalen a {resultado} °C")
    else:
        print("Escala no válida. Debe ingresar C o F.")


if __name__ == "__main__":
    main()