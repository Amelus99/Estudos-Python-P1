# IP 2020.2 - Semana 10

# 5 alunos, cada aluno tem 4 notas

qtde = 0

# declarar a matriz
matriz_notas = []
for i in range(5):
    matriz_notas.append([0] * 4)

print(matriz_notas)

# preencher a matriz com as notas
for i in range(5): # alunos
    print("Aluno:", i + 1)
    for j in range(4): # notas de cada aluno
        #matriz_notas[i][j] = 100
        matriz_notas[i][j] = int(input("Nota {}:".format(j + 1)))

# procurar quantas notas possuem valor acima ou igual a média (70)

for i in range(5):
   for j in range(4):
       if (matriz_notas[i][j] >= 70):
           qtde += 1

print('Quantidade acima da média (70):', qtde)

print(matriz_notas)

for i in range(5):
    for j in range(4):
        print(matriz_notas[i][j])
