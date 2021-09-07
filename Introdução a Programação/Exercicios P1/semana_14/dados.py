# nome, idade, email: [dicionário] --> 4 pessoas
# dois, quatro, tres, um

def ordenar(lista):
    lista_local = lista.copy()
    for i in range(len(lista_local) - 1):
        menor = i
        for j in range(i + 1, len(lista_local)):
            if (lista_local[j]['nome'] < lista_local[menor]['nome']):
                menor = j
        lista_local[i], lista_local[menor] = lista_local[menor], lista_local[i]
    return lista_local

# programa principal

pessoas = []

for i in range(4):
    pessoa = {}
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    pessoa['email'] = input('e-mail: ')
    pessoas.append(pessoa)

print(pessoas)
copia_ordenada = ordenar(pessoas)
print(pessoas)
print(copia_ordenada)
