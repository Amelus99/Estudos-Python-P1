def index(lista, elem):
    for i in range(len(lista)):
        if (lista[i] == elem):
            return i
    return -1

def count(lista, elem):
    qtde = 0
    for l in lista:
        if (l == elem):
            qtde += 1
    return qtde

def upper(st):
    aux = ''
    for s in st:
        if (s >= 'a') and (s <= 'z'):
            aux += chr(ord(s) - 32)
        else:
            aux += s
    return aux

def isNum(st):
    for s in st:
        if (s < '0') or (s > '9'):
            return False
    return True

def vogais(st):
    letras = 'aeiouAEIOU'
    qtde = 0

    for s in st:
        if (s in letras):
            qtde += 1
    return qtde

# Programa Principal
numeros = [10,20,30,40,50,60,20,40]
frase = 'Instituto Federal - 2021'

print(index(numeros, 20))
print(index(numeros, 200))
print(count(numeros, 20))
print(count(numeros, 200))
print(upper(frase))
print(isNum(frase))
print(vogais(frase))
