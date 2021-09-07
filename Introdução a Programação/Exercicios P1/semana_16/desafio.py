def menu():
    print('1 - Cadastrar')
    print('2 - Listar')
    print('3 - Procurar')
    print('4 - Sair')
    print('Informe sua opção: ')

def procurar(ip):
    try:
        arq = open('dispositivos.csv', 'r')
        for linha in arq.read().splitlines():
            if (linha.split(',')[1] == ip):
                return True
        arq.close()
        return False
    except:
        return False

def cadastrar(disp):
    if (procurar(disp['ip']) == False):
        arq = open('dispositivos.csv', 'a')
        arq.write("{},{},{},{}\n".format(disp['hostname'], disp['ip'], disp['so'], disp['descricao']))
        arq.close()

def listar():
    try:
        arq = open('dispositivos.csv', 'r')
        for linha in arq.read().splitlines():
            print(linha.split(','))
        arq.close()
    except:
        print("Nenhum dispositivo cadastrado!")


# Programa Principal

menu()
opcao = input()
while (opcao != '4'):
    if (opcao == '1'):
        disp = {}
        disp['hostname'] = input('Hostname: ')
        disp['ip'] = input('ip')
        disp['so'] = input('Sistema operacional: ')
        disp['descricao'] = input('Descrição: ')
        cadastrar(disp)
    elif (opcao == '2'):
        listar()
    elif (opcao == '3'):
        ip = input('Informe o endereço IP: ')
        if (procurar(ip) == True):
            print('Endereço IP cadastrado.')
        else:
            print('Endereço IP não cadastrado')
    else:
        print('Opção Inválida.')

    menu()
    opcao = input()

