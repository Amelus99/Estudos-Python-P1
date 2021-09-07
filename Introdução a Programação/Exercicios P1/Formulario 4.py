#Parte I
estados = []
for i in range(27):
    valores = {}
    valores['cod']=input('Cod IBGE: ')
    valores['nome']=input('Nome: ')
    valores['sigla']=input('Sigla: ')
    valores['regiao']=input('Região: ')
    valores['populacao']=int(input('População: '))
    estados.append(valores)
#Parte II - populoso
def populoso(list):
    maior = list[0]
    for i in range(1, len(list)):
        if list[i]['pop'] > maior['pop']:
            maior = list[i]
    return maior
#Parte II - estados
def states(list, reg):
    estados = []
    for estado in list:
        if estado['reg'] == reg:
            estados.append(estado)
    return estados
#Parte II - media
def media(list):
    soma = 0
    for estado in list:
        soma += estado['pop']
    return soma / len(list)
#Parte II - acima
def acima(list):
    lista = []
    for estado in list:
        if estado['pop'] > media(list):
            lista.append(estado)
    return lista
#Parte III
from dados import populoso
from dados import states
from dados import media
from dados import acima

estados = []
for i in range(27):
    valores = {}
    valores['cod']=input('Cod IBGE: ')
    valores['nome']=input('Nome: ')
    valores['sigla']=input('Sigla: ')
    valores['reg']=input('Região: ')
    valores['pop']=int(input('População: '))
    estados.append(valores)

print("POPULOSO:\n",populoso(estados))

print("NORTE:\n",states(estados, "Norte"))

print("MEDIA:\n",media(estados))

print("ACIMA:\n",acima(estados))