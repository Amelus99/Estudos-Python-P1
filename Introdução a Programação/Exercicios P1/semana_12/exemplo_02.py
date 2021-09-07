st = 'ifpb 2021'

# contar
print(st.count('2'))
print(st.count(' '))
print(st.count('f'))
print(st.count('x'))
quantidade = st.count('d')

qtde = 0
for i in range(len(st)):
    if (st[i] == '2'):
        qtde += 1

print(st.find('2'))
print(st.find('i'))
print(st.find('x'))

posicao = -1
for i in range(len(st)):
    if (st[i] == '2'):
        posicao = i
        break

