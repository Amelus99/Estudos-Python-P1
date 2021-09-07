valor = int(input())

c_100 = valor // 100
troco = valor % 100

c_50 = troco // 50
troco = troco % 50

c_20 = troco // 20
troco = troco % 20

c_10 = troco // 10
troco = troco % 10

c_5 = troco // 5
troco = troco % 5

c_2 = troco // 2
c_1 = troco % 2

print(valor)
print(c_100, 'nota(s) de R$ 100,00')
print(c_50, 'nota(s) de R$ 50,00')
print(c_20, 'nota(s) de R$ 20,00')
print(c_10, 'nota(s) de R$ 10,00')
print(c_5, 'nota(s) de R$ 5,00')
print(c_2, 'nota(s) de R$ 2,00')
print(c_1, 'nota(s) de R$ 1,00')
