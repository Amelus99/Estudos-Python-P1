def frequencia(st):
    freq = {}
    for s in st:
        if (s not in freq.keys()):
            freq[s] = 1
        else:
            freq[s] += 1
    return freq

# programa principal

frase = input()
print(frequencia(frase))
