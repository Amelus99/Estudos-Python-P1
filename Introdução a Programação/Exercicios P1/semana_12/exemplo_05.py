def somar(lista):
    total = 0
    for i in range(len(lista)):
        total += lista[i]
    return total

def media(lista):
    return somar(lista)/len(lista)

def quantidade_acima(lista):
    m = media(lista)
    qtde = 0
    for i in range(len(lista)):
        if (lista[i] > m):
            qtde += 1
    return qtde

# lista -> parâmetro da função
# escopo é local! Só pode usar dentro da função
# qtde - escopo é local!
def quantidade_abaixo(lista):
    m = media(lista)
    qtde = 0
    for i in range(len(lista)):
        if (lista[i] < m):
            qtde += 1
    return qtde


# programa principal
numeros = [10,20,30,40,50,60,70,80,90,100]

# soma dos números
print(somar(numeros))

# média dos números
print(media(numeros))

# quantidade de números com valor acima da média
print(quantidade_acima(numeros))

# quantidade de números com valor abaixo da média
print(quantidade_abaixo(numeros))
