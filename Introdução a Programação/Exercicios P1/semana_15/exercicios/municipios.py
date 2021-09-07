from pprint import pprint

arq = open('municipios.csv', 'r')

municipios = {}

for linha in arq.read().splitlines():
    lista = linha.split(',')
    dados = {}
    dados['nome'] = lista[0]
    dados['gentilico'] = lista[2]
    dados['area'] = int(lista[3])
    dados['populacao'] = int(lista[4])
    dados['densidade'] = float(lista[5])
    municipios[int(lista[1])] = dados

arq.close()

pprint(municipios[2507507])
pprint(municipios[2507507]['nome'])

total = 0
for m in municipios.values():
    #total += municipios[m]['populacao']
    total += m['populacao']

print(total)
