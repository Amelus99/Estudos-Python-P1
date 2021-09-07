'''
    Para ler um número inteiro positivo (acima de zero).
    Eu só aceito um valor positivo (acima de zero)
'''

num = int(input('Número: '))
while (num <= 0):
    num = int(input('Número: '))

print('Número:', num)
