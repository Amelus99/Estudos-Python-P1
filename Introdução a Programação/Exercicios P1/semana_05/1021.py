valor = float(input())

valor_int = int(valor)
valor_real = valor - valor_int
valor_real_int = int(valor_real * 100)

print(valor_int, valor_real_int)
