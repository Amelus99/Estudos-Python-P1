arq = open('nomes.txt', 'r')

# readlines: retorna uma lista contendo o conteúdo do arquivo separaro por linhas.
# cada linha é um índice na lista
dados = arq.readlines()
print(dados)

arq.close()
