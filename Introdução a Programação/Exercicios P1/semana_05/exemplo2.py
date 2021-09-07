'''
    Objetivo: Ler dois número inteiros e informar o maior valor. Informar se houver empate.
'''

n1, n2 = input().split()
n1, n2, = int(n1), int(n2)

# primeira alternativa

if (n1 > n2):
    print(n1, 'é o maior')
else:
    if (n2 > n1):
        print(n2, 'é o maior')
    else:
        print('são iguais')


# segunda alternativa

if (n1 > n2):
    print(n1, 'é o maior')
elif (n2 > n1):
    print(n2, 'é o maior')
else:
    print('são iguais')
