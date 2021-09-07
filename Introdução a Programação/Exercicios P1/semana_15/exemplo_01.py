# w: escrever (criar/recriar)
# r: ler
# a: escrever (no final)

arq = open('dados.txt', 'w')
lista = ['um', 'dois', 'três', 'quatro']

arq.write('que bom!\n')
arq.write('funciona\n')
arq.write('eita\n')
arq.writelines(lista)

arq.close()
