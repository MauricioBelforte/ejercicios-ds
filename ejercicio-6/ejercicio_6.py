"""
Ejercicio 6 — Menú interactivo

Cree un programa que muestre un **menú interactivo** utilizando la estructura `match`:

- **a.** Calcular la suma de los primeros **N** números naturales (usando un `for`).
- **b.** Encontrar todos los números **divisibles por 3** en un rango dado por el usuario (ver `range()`).
- **c.** Salir.
"""


def suma_primeros_naturales(n):
    """Calcula la suma de los primeros N números naturales."""
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma


def divisibles_por_3(inicio, fin):
    """Encuentra todos los números divisibles por 3 en un rango [inicio, fin]."""
    divisibles = []
    for num in range(inicio, fin + 1):
        if num % 3 == 0:
            divisibles.append(num)
    return divisibles


def main():
    while True:
        print("\n--- Menú interactivo ---")
        print("a. Calcular la suma de los primeros N números naturales")
        print("b. Encontrar números divisibles por 3 en un rango")
        print("c. Salir")

        opcion = input("Seleccione una opción: ").lower()

        match opcion:
            case "a":
                n = int(input("Ingrese N: "))
                print(f"La suma de los primeros {n} números naturales es: {suma_primeros_naturales(n)}")
            case "b":
                inicio = int(input("Ingrese el inicio del rango: "))
                fin = int(input("Ingrese el fin del rango: "))
                resultado = divisibles_por_3(inicio, fin)
                print(f"Números divisibles por 3 en [{inicio}, {fin}]: {resultado}")
            case "c":
                print("Nos vemos!")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()