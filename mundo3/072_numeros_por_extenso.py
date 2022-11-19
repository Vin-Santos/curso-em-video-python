"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

Desafio: altere o programa perguntando se o usuário deseja continuar.
"""

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 
'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 
'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

continuar = ' '
while continuar != 'N':
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if numero >= 0 and numero <= 20:
            print(f'Você escolheu: {extenso[numero]}')
            break
    while continuar != 'S':
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'S':
        continuar = ' '
