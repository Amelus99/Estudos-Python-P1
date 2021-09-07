opc = input("'w' para inserir um novo dispositivo"
            "\n'r' para ler o arquivo csv"
            "\n'end' para finalizar todo o processo"
            "\nSelecione: ")
while opc != 'end':
    endereço = {}
    while opc != 'r':
        if opc == 'w':
            ip = input('Endereço IP: ')
            while len(ip) > 15:
                print('Endereço ipv4 maximo 15 digitos')
                ip = input('Endereço IP: ')
            while ip in endereço:
                print('IP já existente digite um novo. ')
                ip = input('Endereço IP: ')

            hostname = input('Hostname: ')
            while not hostname.isalnum():
                print('Não é alfanumerico digite um novo.')
                hostname = input('Hostname: ')

            SO = input('OS: ')
            while not SO.isalnum():
                print('Não é alfanumerico digite um novo.')
                SO = input('OS: ')

            Desc = input('Descrição: ')
            while not Desc.isalnum():
                print('Não é alfanumerico digite um novo.')
                Desc = input('Descrição: ')

            endereços = open('SamIPs.csv', 'a', encoding='utf-8')
            endereços.write(f"{ip},{hostname},{SO},{Desc}\n")
            endereços.close()
            break
        else:
            print("Digite uma opção valida!")
            break

    endereços = open('SamIPs.csv', 'r', encoding='utf-8')
    for i in endereços.read().splitlines():
        aux = i.split(',')

        dados = {'ip': aux[0],
                 'hostname': aux[1],
                 'SO': aux[2],
                 'descrição': aux[3]}
        endereço[aux[0]] = dados
    endereços.close()
    if opc == 'r':
        opc2 = input("'l' para listar todos os dispositivos"
                     "\n'e' para selecionar um IP"
                     "\nSelecione: ")
        if opc2 == 'l':
            endereços = open('SamIPs.csv', 'r', encoding='utf-8')
            for device in endereços.read().splitlines():
                print(device)
            endereços.close()
        if opc2 == 'e':
            print('Digite fim para sair.')
            valor = input('Digite um IP valido: ')
            while valor != 'fim':
                if valor in endereço:
                    print(endereço[valor])
                    print('Digite fim para sair.')
                    valor = input('Digite um IP: ')
                else:
                    print('Digite fim para sair.')
                    valor = input('Digite um IP valido: ')

    opc = input("'w' para inserir um novo dispositivo"
                "\n'r' para ler o arquivo csv"
                "\n'end' para finalizar todo o processo"
                "\nSelecione: ")
