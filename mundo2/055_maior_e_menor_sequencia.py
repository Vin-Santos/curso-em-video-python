"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
peso = float(input('Qual o peso da 1ª pessoa? (em k/gm) '))
peso_maior = peso
peso_menor = peso
for pessoa in range(2, 6):
    novo_peso = float(input(f'Qual o peso da {pessoa}ª pessoa? (em k/gm) '))
    if novo_peso < peso_maior:
        peso_maior = novo_peso
    if novo_peso > peso_menor:
        peso_menor = novo_peso
print(f'Dentre todos os pesos, o maior é {peso_maior}')
print(f'Dentre todos os pesos, o menor é {peso_menor}')
