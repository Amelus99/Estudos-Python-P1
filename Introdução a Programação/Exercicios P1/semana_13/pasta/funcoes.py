def somar(lista):
    total = 0
    for i in range(len(lista)):
        total += lista[i]
    return total

def media(lista):
    return somar(lista)/len(lista)

def quantidade_acima(lista):
    m = media(lista)
    qtde = 0
    for i in range(len(lista)):
        if (lista[i] > m):
            qtde += 1
    return qtde

def quantidade_abaixo(lista):
    m = media(lista)
    qtde = 0
    for i in range(len(lista)):
        if (lista[i] < m):
            qtde += 1
    return qtde
