lista = [10, 20, 30, 10, 50, 60, 10, 80, 90, 100]

print(lista)
print(lista[0])
print(lista[9])
print(lista[0:5])
print(lista[2:5])
print(lista[0], lista[1], lista[5:7], lista[9])

lista.remove(30)
print(lista, len(lista))

lista.remove(10)
print(lista, len(lista))

del(lista[0:3])
print(lista, len(lista))
