# vogais

qtde = 0
frase = input("Frase: ")
vogais = 'aeiouAEIOU'

for i in range(len(frase)):
    #if (frase[i] in vogais):
    for j in range(len(vogais)):
        if (frase[i] == vogais[j]):
            qtde += 1
            break

print(qtde)
