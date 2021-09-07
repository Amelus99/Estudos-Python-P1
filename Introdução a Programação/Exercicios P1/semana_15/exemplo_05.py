arq = open('nomes.txt', 'r')

dados = arq.read()

#print(dados.split('\n'))

# print(dados.split('\n').index('Ian'))

for nome in dados.split('\n'):
    print(nome)

arq.close()
