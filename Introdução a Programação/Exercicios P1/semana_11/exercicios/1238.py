qtde = int(input())

for i in range(qtde):
    st1, st2 = input().split(' ')

    menor = min(len(st1), len(st2))
    for i in range(menor):
        print(st1[i], end='')
        print(st2[i], end='')
    if (len(st1) <= len(st2)):
        print(st2[len(st1):])
    else:
        print(st1[len(st2):])
