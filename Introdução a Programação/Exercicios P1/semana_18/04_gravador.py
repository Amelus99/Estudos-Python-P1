def mensagem_oculta(st):
    temp = ''
    for s in st.split():
        temp += s[0]
    return  temp

# Programa Principal

lista = []
arq = open('textos.txt', 'a')

texto = input("Texto: ")
palavra = mensagem_oculta(texto)
while (palavra not in lista):
    lista.append(palavra)
    arq.write(texto)
    arq.write("\n")
    texto = input("Texto: ")
    palavra = mensagem_oculta(texto)

arq.close()
print(lista)
