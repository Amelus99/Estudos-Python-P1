# Converter em maiúsculo
# minúsculo: [97 - 122]

palavra = input('Palavra: ')
nova_palavra = ''

for i in range(len(palavra)):
    #if (ord(palavra[i]) >= 97) and (ord(palavra[i]) <= 122):
    if (palavra[i] >= 'a') and (palavra[i] <= 'z'):
        nova_palavra += chr(ord(palavra[i]) - 32)
    else:
        nova_palavra += palavra[i]

print(palavra)
print(nova_palavra)
