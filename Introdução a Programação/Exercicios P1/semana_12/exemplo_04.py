# funções
def minha_count(st, s):
    qtde = 0
    for i in range(len(st)):
        if (st[i] == s):
            qtde += 1
    return qtde

def minha_find(st, s):
    for i in range(len(st)):
        if (st[i] == s):
            return i
    return -1


# programa principal
frase = input('Informe uma frase: ')
simbolo = input('Informe um símbolo: ')

# exibir a frequência da letra f
print(minha_count(frase, simbolo))

# exibir a posição da letra 'm'
print(minha_find(frase, 'm'))
