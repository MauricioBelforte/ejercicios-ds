"""
Ejercicio 5 — Validación de contraseña

Escriba un programa que solicite al usuario una **contraseña**. Utilizar **operadores
lógicos** y métodos de strings (`.isupper()`, `.islower()`, `len()`) para verificar si
cumple con tres condiciones básicas:

- **a.** Tiene al menos **8 caracteres**.
- **b.** Contiene al menos una **letra mayúscula**.
- **c.** Al menos una **minúscula**.

Imprimir un mensaje adecuado al caso.
"""


def main():
    contrasena = input("Ingrese una contraseña: ")

    tiene_longitud = len(contrasena) >= 8
    tiene_mayuscula = any(c.isupper() for c in contrasena)
    tiene_minuscula = any(c.islower() for c in contrasena)

    if tiene_longitud and tiene_mayuscula and tiene_minuscula:
        print("La contraseña es válida.")
    else:
        print("La contraseña no cumple con los requisitos:")
        if not tiene_longitud:
            print("- Debe tener al menos 8 caracteres.")
        if not tiene_mayuscula:
            print("- Debe contener al menos una letra mayúscula.")
        if not tiene_minuscula:
            print("- Debe contener al menos una letra minúscula.")


if __name__ == "__main__":
    main()