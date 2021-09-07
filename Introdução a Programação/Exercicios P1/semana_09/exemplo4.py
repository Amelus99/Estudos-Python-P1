numeros = []
soma = 0

num = int(input())
while (num != 0):
    numeros.append(num)
    soma += num
    num = int(input())

for i in range(len(numeros)):
    if (numeros[i] > soma/len(numeros)):
        print(numeros[i])

print(numeros, len(numeros))
