qtde = int(input())

for i in range(qtde):
    dieta = list(input())
    cafe = list(input())
    almoco = list(input())
    cheater = False
    for i in range(len(cafe)):
        if (cafe[i] in dieta):
            dieta.remove(cafe[i])
        else:
            cheater = True
            break
    if (cheater == False):
        for i in range(len(almoco)):
            if (almoco[i] in dieta):
                dieta.remove(almoco[i])
            else:
                cheater = True
                break
    if (cheater):
        print('CHEATER')
    else:
        dieta.sort()
        for i in range(len(dieta)):
            print(dieta[i], end='')
        print()
