"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

valor = int(input('Qual valor você deseja sacar? (somente valor inteiro) R$'))
cinquenta = vinte = dez = um = 0

while valor >= 50:
    valor -= 50
    cinquenta += 1
    if valor < 50:
        print(f'Serão entregues {cinquenta} notas de R$50.')
while valor < 50 and valor >= 20:
    valor -= 20
    vinte += 1
    if valor < 20:
        print(f'Serão entregues {vinte} notas de R$20.')
while valor < 50 and valor < 20 and valor >= 10:
    valor -= 10
    dez += 1
    if valor < 10:
        print(f'Serão entregues {dez} notas de R$10.')
while valor < 10 and valor >=1:
    valor -= 1
    um += 1
    if valor < 1:
        print(f'Serão entregues {um} notas de R$1')

# Esse foi o resultado que cheguei, mas no video de correção o professor Guanabara utilizou outra forma de resolver usando "while True" e condicionais, vale a pena dar uma olhada.
