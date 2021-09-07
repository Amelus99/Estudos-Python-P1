#dicionario = {}
#dicionario = dict()
pessoa = {}

# nome, idade, email, telefone

pessoa['nome'] = 'Valéria'
pessoa['idade'] = 15
pessoa['email'] = 'valeria.cavalcanti@ifpb.edu.br'
pessoa['telefone'] = '12345678'

print(pessoa)

pessoa['nome'] = 'Paulo Ditarso'
print(pessoa)

pessoa['idade'] += 1

print(pessoa)

print(pessoa.keys())
print(pessoa.items())
