'''
    Ler várias notas. Calcular e exibir, quantas notas são válidas [0,100].
    Codição de parada: valor negativo
    Cenário de Teste: 80 90 100 120 0 -1
'''

qtde = 0

nota = int(input('Nota: '))
while (nota >= 0):
    if (nota <= 100):
        qtde += 1
    nota = int(input('Nota: '))

print('Quantidade:', qtde)
