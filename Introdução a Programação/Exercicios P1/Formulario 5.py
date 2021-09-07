#Arquivo CSV Municipios da PB

#Programa
municipios = open('Municípios da PB - Página1.csv', 'r', errors='ignore')
# foi retirada a primeira linha do arquivo csv correspondente aos nomes das tabelas
aux = []
muni = []

for nome in municipios.read().splitlines():
    aux = nome.split(',')
    municipio = {'cod': (aux[1]),
                 'nome': aux[0],
                 'gent': aux[2],
                 'area': int(aux[3]),
                 'pop': int(aux[4]),
                 'dens': float(aux[5])}
    muni.append(municipio)
print(muni)

codigo = input('Digite um codigo valido: ')
print('Digite fim para sair.')
while codigo != 'fim':
    for i in range(223):
        if muni[i]['cod'] == codigo:
            print(muni[i])
    codigo = input('Digite um codigo: ')
    print('Digite fim para sair.')


municipios.close()