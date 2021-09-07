import random

numeros = []

while(len(numeros) < 6):
    num = random.randint(1, 60)
    if (not num in numeros):
        numeros.append(num)

print(numeros)
