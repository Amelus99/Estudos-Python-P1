#import funcoes
from pasta.funcoes import somar
from pasta.funcoes import media
from pasta.funcoes import quantidade_acima
from pasta.funcoes import quantidade_abaixo

# programa principal
numeros = [10,20,30,40,50,60,70,80,90,100]

# soma dos números
print(somar(numeros))

# média dos números
print(media(numeros))

# quantidade de números com valor acima da média
print(quantidade_acima(numeros))

# quantidade de números com valor abaixo da média
print(quantidade_abaixo(numeros))
