"""
Crie um programa que vai gerar cinco números aleatórios e colocar e uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint

aleatorios = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

maior = aleatorios[0]
menor = aleatorios[0]
for num in aleatorios:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f'A lista sorteada foi: {aleatorios}')
print(f'O maior deles é: {maior}')
print(f'O menor deles é: {menor}')

