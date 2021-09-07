def sum(list):
    soma = 0
    for i in range(len(list)):
        soma += list[i]
    return soma


def mid(list):
    return sum(list) / len(list)


def distinct(list):
    n=0
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] == list[j] and i != j:
                n+=1
    if n>=1:
        return 'Possui numeros iguais.'
    else:
        return 'Numeros distintos.'


def big(list):
    bg = -1
    for i in range(len(list)):
        n = list[i]
        if n > bg:
            bg = list[i]
    return bg


def small(list):
    sm = big(list)
    for i in range(len(list)):
        n = list[i]
        if n < sm:
            sm = list[i]
    return sm


def order(list):

    if list == sorted(list) or list == sorted(list, reverse=True):
        return 'Está ordenada.'
    else:
        return 'Não está ordenada.'