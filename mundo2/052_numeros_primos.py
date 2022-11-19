"""
Faça um programa que leia um número inteiro e diga se ele é ou não um primo.
"""
numero = int(input('\033[33mDigite um número:\033[m '))

contador = 0
for c in range(1, numero + 1, 1):
    primo = numero % c
    if primo == 0:
        contador += 1
if contador != 2:
    print(f'O número {numero} não é primo!')
else:
    print(f'O número {numero} é primo!')
    