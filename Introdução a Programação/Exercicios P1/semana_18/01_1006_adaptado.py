n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))
n3 = int(input('Nota 3: '))

media = ((n1 * 3) + (n2 * 3) + (n3 * 4)) / 10

print("Média = {}".format(media))

if (media >= 70):
    print("Aprovado")
elif (media >= 40):
    print("Final")
else:
    print("Reprovado")
