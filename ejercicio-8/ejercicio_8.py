"""
Ejercicio 8 — calcular_precio_final()

Escribir un programa que contenga una función `calcular_precio_final(precio_base, porcentaje_descuento=10, es_vip=False)`.

- **a.** Si el cliente es VIP (`es_vip=True`), se le descuenta un **5% extra** sobre el precio ya rebajado.
- **b.** Validar que los valores ingresados sean **positivos** (lanzar una excepción `ValueError` si esto no es así).

Invocar a la función **varias veces** con diferentes parámetros para comprobar el funcionamiento correcto.
"""


def calcular_precio_final(precio_base, porcentaje_descuento = 10, es_vip = False):
    """Calcula el precio final aplicando un descuento y un extra VIP si corresponde."""
    if precio_base < 0 or porcentaje_descuento < 0:
        raise ValueError("El precio base y el porcentaje de descuento deben ser positivos.")

    precio_rebajado = precio_base * (1 - porcentaje_descuento / 100)

    if es_vip:
        precio_rebajado *= 0.95  # 5% extra de descuento

    return precio_rebajado


def main():
# --- PRUEBAS DE LA FUNCIÓN ---
    
    # Caso 1: Solo precio base (usa descuento por defecto del 10% y VIP False)
    print("Caso 1 (Por defecto):", calcular_precio_final(1000))  
    # 1000 - 10% = 900
    
    # Caso 2: Con descuento (20%)
    print("Caso 2 (Descuento 20%):", calcular_precio_final(1000, 20)) 
    # 1000 - 20% = 800

    # Caso 3: Cliente VIP (Descuento 10% por defecto + 5% VIP)
    # Con (es_vip=True) para saltarnos el porcentaje_descuento
    print("Caso 3 (Cliente VIP):", calcular_precio_final(1000, es_vip=True)) 
    # 1000 - 10% = 900 -> 900 - 5% = 855

    # Caso 4: Con (Descuento 50% + VIP)
    print("Caso 4 (50% + VIP):", calcular_precio_final(1000, 50, True)) 
    # 1000 - 50% = 500 -> 500 - 5% = 475

    # Caso 5: (ValueError) con un try/except
    print("\nCaso 5 (Forzando error):")
    try:
        calcular_precio_final(-500, 10)
    except ValueError as error:
        print(f"Error capturado: {error}")

if __name__ == "__main__":
    main()