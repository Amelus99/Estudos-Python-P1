arq = open('nomes.txt', 'r')

dados = arq.read()
print(dados)

# posiciona o cursor no início do arquivo
arq.seek(0)

dados = arq.read()
print(dados)

arq.close()
