# 1 - Escreva um programa para ler 10 números. Exiba todos os números ímpares que foram digitados.
lista = []
for i in range(10):
    x = int(input())
    if x % 2 != 0:
        lista.append(x)
print (lista)

# 2 - Escreva um programa para ler vários números. Exiba todos os números informados que possuem valor acima da média dos números lidos.
s = 0
l = []
n = 1

while n != 0:
    n = int(input())
    if n != 0:
        l.append(n)
        s = s + n

m = s / len(l)

print("{:.2f}".format(m))

for i in range(len(l)):
    if(l[i] > m):
        print(l[i])
# 3 - Escreva um programa para ler 6 (seis) números. Seu programa deverá informar se os números lidos são distintos, ou seja, não repetem.
l = []
max = -1
for i in range(6):
    x = int(input())
    l.append(x)
    if (x > max):
        max = x

for i in range(0, max+1 , 1):
    l.count(i)
    if l.count(i) >= 2:
        print("Valor repete")
        print(i, "x",l.count(i))
# 4 - Escreva um programa para ler 6 (seis) números inteiros distintos. O algoritmo deverá ignorar valores que já foram informados e solicitar outro.  O programa deverá encerrar quando os 6 valores forem lidos.
# 5 - Escreva um programa para ler 10 (dez) números pertencentes ao intervalo [1,100]. Gere um valor aleatório entre [1,100], calcule e exiba quantas vezes esse valor aleatório aparece nos números que foram digitados.
# https://docs.python.org/3.7/library/random.html
