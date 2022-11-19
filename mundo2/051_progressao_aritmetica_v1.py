"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""
print('\033[34m-=- \033[m' * 6)
print('\033[34mProgressão Aritimética\033[m')
print('\033[34m-=- \033[m' * 6)

primeiro = int(input('\033[33mDigite o primeiro termo:\033[m '))
razao = int(input('\033[33mDigite a razão a ser seguida:\033[m'))

for pa in range(primeiro, (primeiro + (10 - 1) * razao) + 1, razao):
    print(pa)
    primeiro += 1
