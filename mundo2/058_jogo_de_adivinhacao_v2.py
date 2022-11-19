"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
from time import sleep

print('\nVou pensar em um número de 0 à 10...')
numero_sorteado = randint(0, 10)
sleep(3)
print('Pensei! Agora tente adivinhar.\n')
sleep(2)

palpite = int(input('\033[35mEm qual número eu pensei?\033[m '))
contador = 0
while palpite != numero_sorteado:
    palpite = int(input('\033[31mErrou, tente de novo:\033[34m '))
    sleep(0.5)
    contador += 1
print(f'\033[32mVocê precisou de {contador} tentativas, mas acertou, pensei no número {numero_sorteado}. Parabéns!\033[m\n')

