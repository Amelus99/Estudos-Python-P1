arq = open('nomes.txt', 'a')

nome = input('Nome: ')
while (nome.upper() != "FIM"):
    arq.write(nome + '\n')
    nome = input('Nome: ')

arq.close()
