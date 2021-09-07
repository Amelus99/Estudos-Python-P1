# Nesta questão, faltou informar o critério de parada.
# Vamos considerar qualquer critério adotado.
# Nesse exemplo, vamos considerar que vai parar quando for informado valor 0 (zero)

numeros = []
soma = 0

# Ler vários números. Encerra quando for informado 0 (zero)
num = int(input('Valor: '))
while (num != 0):
    numeros.append(num)
    soma += num
    num = int(input('Valor: '))

# Caso tenha sido informado algum valor diferente de zero
if (len(numeros) > 0):
    # calcula a média
    media = soma / len(numeros)

    # verifica quais números possuem valor acima dessa média calculada
    for i in range(len(numeros)):
        if (numeros[i] > media):
            print(numeros[i])
else:
    print('Não foi informado valor válido.')
