numeros = [0] * 10

# Ler os 10 valores
for i in range(10):
    numeros[i] = int(input('Número: '))

# Exibir os números ímpares digitados
for i in range(10):
    if (numeros[i] % 2 == 1):
        print(numeros[i])
