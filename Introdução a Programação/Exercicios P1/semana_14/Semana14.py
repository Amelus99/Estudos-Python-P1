from S14Dados import populoso
from S14Dados import states
from S14Dados import media
from S14Dados import acima

estados = []
for i in range(2):
    valores = {}
    valores['cod']=input('Cod IBGE: ')
    valores['nome']=input('Nome: ')
    valores['sigla']=input('Sigla: ')
    valores['reg']=input('Região: ')
    valores['pop']=int(input('População: '))
    estados.append(valores)
print(estados)
print("POPULOSO:\n",populoso(estados))

print("NORTE:\n",states(estados, "Norte"))

print("MEDIA:\n",media(estados))

print("ACIMA:\n",acima(estados))