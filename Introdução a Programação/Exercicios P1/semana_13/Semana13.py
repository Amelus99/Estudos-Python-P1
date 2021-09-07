from S13Dados import sum
from S13Dados import mid
from S13Dados import distinct
from S13Dados import big
from S13Dados import small
from S13Dados import order

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
