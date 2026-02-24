# Solicitar el número al usuario
try:
    numero = int(input("Introduce un número entero: "))

    # Verificar paridad con el operador módulo %
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")
except ValueError:
    print("Por favor, introduce un número entero válido.")
