def soma(lista):
    total = 0
    for elem in lista:
        total += elem
    return total

def media(lista):
    return soma(lista)/len(lista)

def distintos(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if (lista[i] == lista[j]):
                return False
    return True

def maior(lista):
    aux = lista[0]
    for i in range(1, len(lista)):
        if (lista[i] > aux):
            aux = lista[i]
    return aux

def menor(lista):
    aux = lista[0]
    for i in range(1, len(lista)):
        if (lista[i] < aux):
            aux = lista[i]
    return aux

def ordenado(lista):
    for i in range(len(lista) - 1):
        if (lista[i] > lista[i + 1]):
            return False
    return True
