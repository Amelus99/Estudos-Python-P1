#Programa
from pprint import pprint

municipios = open('Municípios da PB - Página1.csv', 'r', encoding='utf-8')

municipio = {}

for nome in municipios.read().splitlines():
    aux = nome.split(',')
    dados = {'nome': aux[0],
             'gent': aux[2],
             'area': int(aux[3]),
             'pop': int(aux[4]),
             'dens': float(aux[5])}
    municipio[int(aux[1])] = dados

municipios.close()

codigo = input('Digite um codigo valido: ')
x = int(codigo)
print('Digite fim para sair.')
while codigo != 'fim':
    x = int(codigo)
    if x in municipio:
        pprint(municipio[x])
        codigo = input('Digite um codigo: ')
        print('Digite fim para sair.')
    else:
        codigo = input('Digite um codigo valido: ')
        print('Digite fim para sair.')