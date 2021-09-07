numeros = []

# Tentar inserir valores, enquanto a lista estiver com menos de 6
while (len(numeros) < 6):
    num = int(input('Valor: '))
    # Se o número não estiver na lista, adiciona!
    if (num not in numeros):
        numeros.append(num)

print(numeros)
