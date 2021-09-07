#Biblioteca
def sum(list):
    soma = 0
    for i in range(len(list)):
        soma += list[i]
    return soma


def mid(list):
    return sum(list) / len(list)


def distinct(list):
    n=0
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] == list[j] and i != j:
                n+=1
    if n>=1:
        return 'Possui numeros iguais.'
    else:
        return 'Numeros distintos.'


def big(list):
    bg = -1
    for i in range(len(list)):
        n = list[i]
        if n > bg:
            bg = list[i]
    return bg


def small(list):
    sm = big(list)
    for i in range(len(list)):
        n = list[i]
        if n < sm:
            sm = list[i]
    return sm


def order(list):

    if list == sorted(list) or list == sorted(list, reverse=True):
        return 'Está ordenada.'
    else:
        return 'Não está ordenada.'
#Programa Principal
#Programa criado para testar as funções da biblioteca.
from Biblioteca import sum
from Biblioteca import mid
from Biblioteca import distinct
from Biblioteca import big
from Biblioteca import small
from Biblioteca import order

y = []
x = []
n = 1

while n != -1:
    print('Digite -1 para sair.')
    n = float(input('Digite o valor: '))
    ni = int(n)
    if n>=0:
        y.append(n)
        x.append(ni)

print('Soma: ',sum(y))
print('Media: ',mid(y))
print(distinct(y))
print('Maior: ',big(x))
print('Menor: ',small(y))
print(order(y))