municipios = open('Municípios da PB - Página1.csv', 'r', errors='ignore')

aux = []
muni = []

for codes in municipios.read().splitlines():
    aux = codes.split(',')
    muni.append([int(aux[1])])
municipios.seek(0)
i = 0
for dados in municipios.read().splitlines():
    aux = dados.split(',')
    muni[i].append({'cod': int(aux[1]),
                    'nome': aux[0],
                    'gent': aux[2],
                    'area': int(aux[3]),
                    'pop': int(aux[4]),
                    'dens': float(aux[5])})
    i += 1
print(muni)
print(muni[0][0])
codigo = int(input('Digite um codigo: '))
while codigo != 'fim':
    if codigo in muni:
        print()
    codigo = int(input('Digite um codigo: '))

municipios.close()


from pprint import pprint

municipios = open('MunicipiosPB.csv', 'r', encoding='utf-8')

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
