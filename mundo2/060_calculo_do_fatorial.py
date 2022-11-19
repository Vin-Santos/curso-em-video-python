"""
Faça um programa que leia um número qualquer e mostre o seu fatrial.
"""
numero = int(input('Digite um número: '))
contador = numero
fatorado = 1

print(f'{numero}! = ', end = '')
while contador > 0:
    print(f'{contador}', end = '')
    print(' x ' if contador > 1 else ' = ', end = '')
    fatorado = fatorado * contador
    contador -= 1
print(f'{fatorado}')
