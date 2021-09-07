n1, n2 = input().split()
n1, n2 = int(n1), int(n2)

'''
if (n1 > n2):
    aux = n1
    n1 = n2
    n2 = aux
'''

if (n1 > n2):
    n1, n2 = n2, n1

if (n2 % n1 == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
