# ler uma frase - quantidade de palavras

qtde = 0
frase = input('Frase: ')

for i in range(len(frase)):
    if (frase[i] == ' '):
        qtde += 1

print(qtde + 1)
