'''
Para ler 4 números. Calcule e informe a soma dos números lidos!
'''
soma = 0
qtde_pos = 0

qtde = int(input('Quantidade de iterações: '))

for i in range(qtde):
    num = int(input('Informe o {} valor: '.format(i + 1)))
    soma = soma + num
    if (num > 0):
        qtde_pos += 1
    # soma += num

    


print(soma)
