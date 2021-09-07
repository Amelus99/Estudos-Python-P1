'''
simbolos numéricos
simbolos maiusculos
simbolos minusculos
caracteres especiais
'''

qtde_num = qtde_maiuscula = qtde_minuscula = qtde_especial = 0

frase = input('Frase: ')

for i in range(len(frase)):
    if (frase[i] >= 'A') and (frase[i] <= 'Z'):
        qtde_maiuscula += 1
    elif (frase[i] >= 'a') and (frase[i] <= 'z'):
        qtde_minuscula += 1
    elif (frase[i] >= '0') and (frase[i] <= '9'):
        qtde_num += 1
    else:
        qtde_especial += 1

print(qtde_maiuscula)
print(qtde_minuscula)
print(qtde_num)
print(qtde_especial)

# eita que bom! #estudarPYTHON_eh_10
# 6
# 19
# 2
# 7
