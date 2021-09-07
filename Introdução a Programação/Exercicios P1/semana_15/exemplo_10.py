arq = open('estados.csv', 'r')

for linha in arq.read().splitlines():
    print(linha.split(','))

arq.close()
