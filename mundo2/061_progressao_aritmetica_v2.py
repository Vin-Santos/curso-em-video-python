"""
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
print('\033[34m-=- \033[m' * 6)
print('\033[34mProgressão Aritimética\033[m')
print('\033[34m-=- \033[m' * 6)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão para seguir: '))
contador = 0

while contador < 10:
    print(f'{primeiro}', end=' -> ')
    primeiro += razao
    contador +=1
print('FIM!\n')
 