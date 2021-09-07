qtde = 0
n = int(input("N: "))
lista = [0] * n

for i in range(n):
    lista[i] = int(input("Valor: "))

for i in range(n - 1):
    if (lista[i] % lista[n - 1] == 0):
        qtde += 1

print(qtde)
