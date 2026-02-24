def test_verificar_pares_impares():
    numeros = [10, 5, 8, 3, 17, 20]
    esperado = ["par", "impar", "par", "impar", "impar", "par"]
    
    resultado = verificar_pares_impares(numeros)
    
    assert resultado == esperado
