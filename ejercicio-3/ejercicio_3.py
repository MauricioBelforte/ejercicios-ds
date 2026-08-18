"""
Ejercicio 3 — Costo total de un viaje

Escriba un programa que solicite al usuario:

- **a.** El costo estimado de un pasaje.
- **b.** El costo de alojamiento por noche.
- **c.** La cantidad de noches que durará el viaje.
- **d.** El dinero disponible.

El programa debe:
- Calcular el costo total del viaje.
- Determinar (con un booleano) si el dinero disponible es suficiente.
- Mostrar un resumen formateado con los resultados.

> Ver `input()` y **f-strings**.
"""


def main():
    costo_pasaje = float(input("Ingrese el costo estimado del pasaje: "))
    costo_alojamiento_noche = float(input("Ingrese el costo de alojamiento por noche: "))
    cantidad_noches = int(input("Ingrese la cantidad de noches que durará el viaje: "))
    dinero_disponible = float(input("Ingrese el dinero disponible: "))

    costo_total = costo_pasaje + (costo_alojamiento_noche * cantidad_noches)
    es_suficiente = dinero_disponible >= costo_total

    print("\n--- Resumen del viaje ---")
    print(f"Costo del pasaje: ${costo_pasaje}")
    print(f"Costo de alojamiento por noche: ${costo_alojamiento_noche}")
    print(f"Cantidad de noches: {cantidad_noches}")
    print(f"Costo total del viaje: ${costo_total}")
    print(f"Dinero disponible: ${dinero_disponible}")
    print(f"¿El dinero es suficiente? {es_suficiente}")


if __name__ == "__main__":
    main()