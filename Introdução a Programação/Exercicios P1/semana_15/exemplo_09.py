arq = open('nomes.txt', 'r')

for linha in arq.read().splitlines():
    print(linha)

arq.close()
