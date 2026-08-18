"""
Ejercicio 9 — Clase CuentaBancaria

Cree una clase `CuentaBancaria` con los siguientes requisitos:

- **a.** Atributos de instancia: `titular` y `saldo` (por defecto en `0.0`).
- **b.** Método `depositar(monto)`: suma el monto al saldo si es **mayor a 0**.
- **c.** Método `retirar(monto)`: resta el saldo si hay **fondos suficientes**, de lo contrario muestra un **mensaje de error**.
- **d.** Método `mostrar_info()`: imprime el **titular** y el **saldo actual**.

Cree un par de instancias y realice operaciones para probarla.
"""


class CuentaBancaria:
    """Representa una cuenta bancaria simple."""

    def __init__(self, titular, saldo = 0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        """Suma el monto al saldo si es mayor a 0."""
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso: ${monto}. Saldo actual: ${self.saldo}.")
        else:
            print("El monto a depositar debe ser mayor a 0.")

    def retirar(self, monto):
        """Resta el monto del saldo si hay fondos suficientes."""
        if monto > self.saldo:
            print(f"Error: Se intento retirar ${monto} pero los fondos son insuficientes.")
        else:
            self.saldo -= monto
            print(f"Retiro exitoso: ${monto}. Saldo restante: ${self.saldo}.")

    def mostrar_info(self):
        """Imprime el titular y el saldo actual."""
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: ${self.saldo}")


def main():
    # Par de instancias
    cuenta_1 = CuentaBancaria("Ana García", 500.0)
    cuenta_2 = CuentaBancaria("Luis Fernández")

    # Operaciones sobre la cuenta 1
    cuenta_1.mostrar_info()
    cuenta_1.depositar(300.0)
    cuenta_1.retirar(150.0)
    cuenta_1.retirar(10000.0)  # Debería mostrar error
    cuenta_1.mostrar_info()

    print()

    # Operaciones sobre la cuenta 2
    cuenta_2.mostrar_info()
    cuenta_2.depositar(1000.0)
    cuenta_2.retirar(1000.0)
    cuenta_2.mostrar_info()


if __name__ == "__main__":
    main()