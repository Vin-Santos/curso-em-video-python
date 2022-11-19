"""
Faça um programa que leia a soma de todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 à 500.
"""
soma = 0
contador = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        soma += numero
        contador += 1
print(f'A soma de todos os números é {soma}')
print(f'Foram somados {contador} números')
