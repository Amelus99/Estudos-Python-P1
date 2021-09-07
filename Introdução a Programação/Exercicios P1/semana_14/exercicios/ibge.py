import funcoes
from pprint import pprint

estados = []

for i in range(27):
    estado = {}
    estado['ibge'] = input('Código IBGE: ')
    estado['nome'] = input('Nome: ')
    estado['sigla'] = input('Sigla: ')
    estado['regiao'] = input('Região: ')
    estado['populacao'] = int(input('População: '))
    estados.append(estado)

# testando as funções
print("POPULOSO")
pprint(funcoes.populoso(estados))

print("\nESTADOS DO NORDESTE")
pprint(funcoes.estados(estados, 'NORDESTE'))

print("\nMÉDIA")
print(funcoes.media(estados))

print("\nACIMA DA MÉDIA")
pprint(funcoes.acima(estados))
