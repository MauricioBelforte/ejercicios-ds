"""
Ejercicio 11 (ex ejercicio 5)— Simulación de inicio de sesión

Escriba un programa que simule un **inicio de sesión**.

- Definir una contraseña correcta en una constante (ej. `"Admin1234"`).
- **a.** Permitir al usuario intentar ingresarla un **máximo de 3 veces** usando un bucle `while`.
- **b.** Si acierta, mostrar un mensaje de **éxito** y terminar.
- **c.** Si agota los intentos, mostrar un mensaje de **bloqueo** y finalizar el programa.
"""

CONTRASENA_CORRECTA = "Admin1234"
MAX_INTENTOS = 3


def main():
    intentos = 0

    while intentos < MAX_INTENTOS:
        contrasena = input("Ingrese su contraseña: ")

        if contrasena == CONTRASENA_CORRECTA:
            print("¡Inicio de sesión exitoso!")
            return

        intentos += 1
        restantes = MAX_INTENTOS - intentos
        if restantes > 0:
            print(f"Contraseña incorrecta. Le quedan {restantes} intento(s).")
        else:
            print("Se agotaron los intentos. Cuenta bloqueada.")


if __name__ == "__main__":
    main()