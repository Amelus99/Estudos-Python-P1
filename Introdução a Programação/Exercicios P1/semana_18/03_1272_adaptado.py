def mensagem_oculta(st):
    temp = ''
    for s in st.split():
        temp += s[0]
    return  temp

# Programa Principal

lista = []

texto = input("Texto: ")
palavra = mensagem_oculta(texto)
while (palavra not in lista):
    lista.append(palavra)
    texto = input("Texto: ")
    palavra = mensagem_oculta(texto)

print(lista)
