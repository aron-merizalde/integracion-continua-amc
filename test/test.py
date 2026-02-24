def verificar_pares_impares(lista_numeros):
    for numero in lista_numeros:
        if numero % 2 == 0:
            print(f"{numero} es par")
        else:
            print(f"{numero} es impar")

# Ejemplo de uso
mis_numeros = [10, 5, 8, 3, 17, 20]
verificar_pares_impares(mis_numeros)
