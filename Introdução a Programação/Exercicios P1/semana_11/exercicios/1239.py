while(True):
    abriu_i = False
    abriu_b = False

    try:
        texto = input()
        texto_out = ''
        for s in texto:
            if (s == '_'):
                if (not abriu_i):
                    texto_out += '<i>'
                    abriu_i = True
                else:
                    texto_out += '</i>'
                    abriu_i = False
            elif (s == '*'):
                if (not abriu_b):
                    texto_out += '<b>'
                    abriu_b = True
                else:
                    texto_out += '</b>'
                    abriu_b = False
            else:
                texto_out += s
        print(texto_out)
    except EOFError:
        break
