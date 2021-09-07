numeros = [0] * 6

# Ler os valores
for i in range(6):
    numeros[i] = int(input('Valor: '))

# Verificar se são distintos
distintos = True
for i in range(6):
    # Verificar se o números da vez (i) é igual algum valor que
    # está após ele (j) na coleção.
    for j in range(i + 1, 6):
        # Se forem iguais, podemos concluir que a coleção não é distinta
        if (numeros[i] == numeros[j]):
            distintos = False
            break # pode parar de verificar
    if (distintos == False):
        break

if (distintos == True):
    print("Números distintos")
else:
    print("Números não distintos")
