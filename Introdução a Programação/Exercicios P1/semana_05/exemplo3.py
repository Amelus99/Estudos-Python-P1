'''
    Objetivo: Ler média e frequência, calcular e exibir se o aluno está aprovado.
    Condição para estar aprovado:
        - nota superior ou igual a 70
        - frequência superior ou igual a 75
'''

media, freq = input().split()
media, freq = int(media), int(freq)

# primeira alternativa

if (media >= 70):
    if (freq >= 75):
        print('passou')
    else:
        print('não passou')
else:
    print('não passou')

# segunda alternativa - usando condição composta

if ((media >= 70) and (freq >= 75)):
    print('passou')
else:
    print('não passou')
