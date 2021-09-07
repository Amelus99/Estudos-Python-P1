soma = 0
numeros = [0] * 6

for i in range(6):
    numeros[i] = int(input())
    soma += numeros[i]

media = soma / 6

print(numeros)

for i in range(6):
    if (numeros[i] > media):
        print(numeros[i])

print(soma)
print(media)

for i in range(6):
    print(numeros[i])
