"""
Ejercicio 7 — analizar_temperaturas()

Escriba un programa con una función llamada `analizar_temperaturas(registros)` que reciba una
**lista de números** (temperaturas).

- **a.** La función debe retornar en una **sola tupla**: el valor **máximo**, el valor **mínimo**
  y el **promedio** de las temperaturas (ver operaciones con listas).
- **b.** Invocar a la función con datos de prueba e imprimir los resultados **desempaquetándolos**.
"""


def analizar_temperaturas(registros):
    """Retorna una tupla con el máximo, el mínimo y el promedio de las temperaturas."""
    maximo = max(registros)
    minimo = min(registros)
    promedio = sum(registros) / len(registros)
    return maximo, minimo, promedio


def main():
    datos_prueba = [22.5, 18.0, 30.1, 25.4, 19.8, 27.3]

    maximo, minimo, promedio = analizar_temperaturas(datos_prueba)

    print(f"Temperaturas: {datos_prueba}")
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")
    print(f"Promedio: {promedio}")


if __name__ == "__main__":
    main()