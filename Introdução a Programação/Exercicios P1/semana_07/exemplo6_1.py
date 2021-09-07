# URI 1113
# Método aceito: 01

num1, num2 = input().split()
num1, num2 = int(num1), int(num2)

while (num1 != num2):
    if (num1 < num2):
        print('Crescente')
    else:
        print('Decrescente')
    num1, num2 = input().split()
    num1, num2 = int(num1), int(num2)
