'''
    Objetivo: Ler três números inteiros e exibir na ordem decrescente.
'''

n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if (n1 > n2) and (n1 > n3):
    # n1 é o maior
    if (n2 > n3):
        # n2 é o segundo maior
        print(n1, n2, n3)
    else:
        # n3 é o segundo maior
        print(n1, n3, n2)
else:
    # n1 não é o maior
    if (n2 > n3):
        # n2 é o maior de todos
        if (n1 > n3):
            # n1 é o segundo maior
            print(n2, n1, n3)
        else:
            # n3 é o segundo maior
            print(n2, n3, n1)
    else:
        # n3 é o maior de todos
        if (n1 > n2):
            # n1 é o segundo maior
            print(n3, n1, n2)
        else:
            # n2 é o segundo maior
            print(n3, n2, n1)
