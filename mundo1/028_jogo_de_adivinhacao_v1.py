"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5, e peça para o usuário tentar adivimhar o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import uniform
from math import ceil

chute = int(input('Acerte o número de 1 a 5 escolhido pelo PC: '))
sorteio = uniform(0,5)  # Sorteia um número decimal entre 0 e 5
numero = ceil(sorteio)  # Arredonda o número para o menor inteiro

if numero == chute:
    print (f'Parabéns, você venceu, o número é {chute}')
else:
    print (f'Você perdeu, não é {chute}. O número certo é {numero}')

# Pode ser usado o randint() para sortear um número inteiro direto, assim como o professor fez no vídeo de correção.
