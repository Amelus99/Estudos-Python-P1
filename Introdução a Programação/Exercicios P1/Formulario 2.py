# 1 - Função "index"
def positions(str, sym):
    for i in range(len(str)):
        if (str[i] == sym):
            return i
    return -1
# 2 - Função "count"
def contador(str, sym):
    cqtd = 0
    for i in range(len(str)):
        if (str[i] == sym):
            cqtd+=1
    return cqtd
# 3 - Função "upper"
def elevador(str):
    nstr = ''
    for i in range(len(str)):
        if (str[i]>='a') and (str[i]<='z'):
            nstr += chr(ord(str[i])-32)
        else:
            nstr += str[i]
    return nstr
# 4 - Função "isNum"
def numerais(str):
    qtd=0
    for i in range(len(str)):
        if (str[i]>='0') and (str[i]<='9'):
            qtd+=1
    if (qtd == len(str)):
        return True
    else:
        return False
# 5 - Função "vogais"
def vogais(str):
    vqtd = 0
    vog= 'AaEeIiOoUu'
    for i in range(len(str)):
        for v in range(len(vog)):
            if (str[i] == vog[v]):
                vqtd+=1
    return vqtd
# 6 - Programa para testar as funções
def positions(str, sym):
    for i in range(len(str)):
        if (str[i] == sym):
            return i
    return -1

def contador(str, sym):
    cqtd = 0
    for i in range(len(str)):
        if (str[i] == sym):
            cqtd+=1
    return cqtd

def elevador(str):
    nstr = ''
    for i in range(len(str)):
        if (str[i]>='a') and (str[i]<='z'):
            nstr += chr(ord(str[i])-32)
        else:
            nstr += str[i]
    return nstr

def numerais(str):
    qtd=0
    for i in range(len(str)):
        if (str[i]>='0') and (str[i]<='9'):
            qtd+=1
    if (qtd == len(str)):
        return True
    else:
        return False

def vogais(str):
    vqtd = 0
    vog= 'AaEeIiOoUu'
    for i in range(len(str)):
        for v in range(len(vog)):
            if (str[i] == vog[v]):
                vqtd+=1
    return vqtd

text = input('Digite um texto: ')
symbol = input('Digite um simbolo: ')

p = positions(text, symbol)
c = contador(text, symbol)
e = elevador(text)
n = numerais(text)
v = vogais(text)

print('Posição: {}.'.format(p))
print('Quantidade do simbolo escolhido: {}.'.format(c))
print(e)
print('Texto numerico? {}.'.format(n))
print('Quantidade de vogais: {}.'.format(v))