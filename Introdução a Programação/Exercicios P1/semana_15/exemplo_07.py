arq = open('nomes.txt', 'r')

linha = arq.readline()
while (linha != ""):
    print(linha)
    linha = arq.readline()
    
arq.close()
