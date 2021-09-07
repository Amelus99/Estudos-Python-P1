arq = open('arquivo_csv_excel.csv', 'r', encoding='utf-8')

for linha in arq.read().splitlines():
    print(linha)

arq.close()
