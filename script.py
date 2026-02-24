def verificar_pares_impares(lista_numeros):
    resultado = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            resultado.append("par")
        else:
            resultado.append("impar")
    return resultado
