# URI 1113
# Método aceito: 02

while (True):
    num1, num2 = input().split()
    num1, num2 = int(num1), int(num2)

    if (num1 == num2):
        break

    if (num1 < num2):
        print('Crescente')
    else:
        print('Decrescente')
