'''
    Ler vários números inteiros enquanto não for zero.
    Exibir:
    - Quantos números foram informados;
    - A média dos números lidos
'''

qtde = 0
soma = 0

num = int(input('Informe um valor: '))
while(num != 0):
    qtde += 1 # qtde = qtde + 1
    soma += num # soma = soma + num
    num = int(input('Informe um valor: '))

print('Quantidade:', qtde)
print('Número:', num)

if (qtde > 0):
    media = soma / qtde
    print('Soma:', soma)
    print('Média:', media)
else:
    print('você não informou valor.')
