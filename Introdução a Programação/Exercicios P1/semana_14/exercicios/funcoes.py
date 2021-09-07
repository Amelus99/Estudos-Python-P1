def populoso(lista):
    # Primeiro Estado, por enquanto, é o mais populoso
    maior = lista[0]
    # Vamos verificar com os demais!
    for i in range(1, len(lista)):
        if (lista[i]['populacao'] > maior['populacao']):
            maior = lista[i]
    return maior

def estados(lista, regiao):
    aux = []
    for estado in lista:
        if (estado['regiao'] == regiao):
            aux.append(estado)
    return aux

def media(lista):
    soma = 0
    for estado in lista:
        soma += estado['populacao']
    return soma / len(lista)

def acima(lista):
    aux = []
    media_br = media(lista)
    for estado in lista:
        if (estado['populacao'] > media_br):
            aux.append(estado)
    return aux
