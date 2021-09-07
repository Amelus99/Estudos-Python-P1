from random import randint

qtde = 0
numeros = [0] * 100

# Ler os 100 valors
for i in range(100):
    numeros[i] = int(input("Valor: "))

# Gerar um valor aleatório entre [1,100]
numero_aleatorio = randint(1, 100)

# Verificar quantos dos números informados possuem valor igual ao aleatório gerado
for i in range(100):
    if (numeros[i] == numero_aleatorio):
        qtde += 1

print('Número aleatório:', numero_aleatorio)
print('Quantidade =', qtde)
