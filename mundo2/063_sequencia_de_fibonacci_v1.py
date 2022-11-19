"""
Escreva um programa que leia um número n interio qualquer e mostre na tela os n primeiros elementos de uma sequencia de Fibonacci.
"""
print('= ' * 20)
print('{:=^40}'.format (' Sequência de Fibonacci '))
print('= ' * 20)

numero = int(input('Quantos números da sequência você deseja ver? '))
termo1 = 0
termo2 = 1
contador = 3

print(f'{termo1} -> {termo2}', end=' -> ')
while contador <= numero:
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    print(f'{termo3}', end=' -> ')
    contador += 1
print('FIM\n')
