codigo, qtde = input().split()
codigo, qtde = int(codigo), int(qtde)

if (codigo == 1):
    valor = 4
elif (codigo == 2):
    valor = 4.5
elif (codigo == 3):
    valor = 5
elif (codigo == 4):
    valor = 2
else:
    valor = 1.5

total = qtde * valor

print('Total: R$ {:.2f}'.format(total))
