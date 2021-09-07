def frequencia(lista):
    freq = {}
    for i in range(len(lista)):
        if (lista[i] not in freq.keys()):
            freq[lista[i]] = 1
        else:
            freq[lista[i]] += 1
    return freq

# Programa Principal [1, 10]

numeros = []
num = int(input())
while (num != 0):
    numeros.append(num)
    num = int(input())

print(numeros)
print(frequencia(numeros))
