arq = open('nomes.txt', 'r')

dados = arq.read()

# verifica se 'Ian' está no arquivo
if ('Ian' in dados):
    print('presente')
else:
    print('ausente')

print(dados)

arq.close()
