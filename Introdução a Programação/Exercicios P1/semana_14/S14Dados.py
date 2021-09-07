def populoso(list):
    maior = list[0]
    for i in range(1, len(list)):
        if list[i]['pop'] > maior['pop']:
            maior = list[i]
    return maior


def states(list, reg):
    estados = []
    for estado in list:
        if estado['reg'] == reg:
            estados.append(estado)
    return estados


def media(list):
    soma = 0
    for estado in list:
        soma += estado['pop']
    return soma / len(list)


def acima(list):
    lista = []
    for estado in list:
        if estado['pop'] > media(list):
            lista.append(estado)
    return lista
