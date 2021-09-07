def funcao():
    global var_global_2
    print('funcao():', var_global_1)
    print('funcao():', var_global_2)
    var_global_2 = "mensagem original 2 - alterada"
    print('funcao():', var_global_2)

# Programa Principal

var_global_1 = "mensagem original 1"
var_global_2 = "mensagem original 2"
funcao()
print(var_global_1)
print(var_global_2)
