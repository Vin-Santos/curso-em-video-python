"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
soma = 0
contador = 0
for pares in range(1, 7):
    numero = int(input('\033[33mDigite um número: \033[m'))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print(f'A soma dos {contador} números pares digitados é {soma}')
