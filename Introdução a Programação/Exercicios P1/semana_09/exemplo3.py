lista = [10, 20, 10, 10, 50, 60, 10, 80, 10, 100]

existe = False
for i in range(len(lista)):
    if (lista[i] == 10):
        existe = True
        break
while(existe == True):
    lista.remove(10)
    existe = False
    for i in range(len(lista)):
        if (lista[i] == 10):
            existe = True
            break

print(lista, len(lista))
