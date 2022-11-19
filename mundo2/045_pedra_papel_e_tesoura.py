"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import choice
print('\033[34m- - \033[34m' * 4)
print('\033[34mJogo de Jokenpô\033[34m')
print('\033[34m- - \033[34m' * 4)

print("""\033[33mAs alternativas são:\033[m
\033[33m 1 - Pedra\033[m
\033[33m 2 - Papel\033[m
\033[33m 3 - Tesoura\033[m""")
player = int(input('\033[36mQual sua escolha?\033[m '))

pc = choice([1, 2, 3])

# Condições
if player == 1 == pc or player == 2 == pc or player == 3 == pc:
    print('Empate')
elif player == 1 and pc == 2:
    print('Eu escolhi Papel, você Pedra\nEU VENCI!')
elif player == 1 and pc == 3:
    print('Eu escolhi Tesoura, você Pedra\nVOCÊ VENCEU!')
elif player == 2 and pc == 1:
    print('Eu escolhi Pedra, você Papel\nVOCÊ VENCEU!')
elif player == 2 and pc == 3:
    print('Eu escolhi Tesoura, você Papel\nEU VENCI!')
elif player == 3 and pc == 1:
    print('Eu escolhi Pedra, você Tesoura\nEU VENCI!')
elif player == 3 and pc == 2:
    print('Eu escolhi Papel, você Tesoura\nVOCÊ VENCEU!')

# No vídeo de correção o professor utilizou o randint() ao invés do choice().
