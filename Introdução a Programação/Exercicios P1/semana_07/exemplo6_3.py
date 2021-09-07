# URI 1113
# Método aceito: 03

'''
                            ATENÇÃO!
    O try_catch é usado quando existe a leitura de vários valores,
    sem determinar o critério de parada.
'''

while (True):
    try:
        num1, num2 = input().split()
        num1, num2 = int(num1), int(num2)

        if (num1 == num2):
            break

        if (num1 < num2):
            print('Crescente')
        else:
            print('Decrescente')
    except EOFError:
        break
