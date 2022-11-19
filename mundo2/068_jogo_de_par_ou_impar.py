"""
Faça um prrgrama para jogar par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint

vitorias_consecutivas = 0
while True:
    print('\033[34m-=\033[m'*16)
    numero_jogador = int(input('\033[36mEsolha um número de 1 à 10: '))
    numero_computador = randint(1, 10)
    soma_escolhas = numero_jogador + numero_computador
    escolha_jogador = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]

    if soma_escolhas % 2 == 0:
        ganhador = 'Par'
    else:
        ganhador = 'Impar'
    print('\033[34m--\033[m'*16)
    print(f'\033[36mVocê escolheu {numero_jogador}, o computador {numero_computador}. O total de {soma_escolhas} é {ganhador}.\033[m')

    if escolha_jogador in ganhador[0]:
        resultado = '\033[32mVocê VENCEU!\033[m'
    elif escolha_jogador not in ganhador[0]:
        resultado = '\033[31mVocê PERDEU!\033[m'
    if resultado == '\033[32mVocê VENCEU!\033[m':
        print(resultado)
        vitorias_consecutivas += 1
    elif resultado == '\033[31mVocê PERDEU!\033[m':
        print(resultado)
        break
print('\033[34m--\033[m'*16)
print(f'\033[35mVocê conseguiu {vitorias_consecutivas} vitórias consecutivas!\033[m')
