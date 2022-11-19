"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores (considere a maioridade com 21 anos).
"""

from datetime import date
ano_atual = date.today().year
maiores = 0
menores = 0

for pessoa in range(1, 8):
    ano = int(input(f'Em que ano a {pessoa}° pessoa nasceu? '))
    if ano_atual - ano >= 21:
        maiores += 1
    else:
        menores += 1
print(f'Considerando a maioridade com 21 anos, {maiores} pessoas são de maior e {menores} pessoas são de menor.')
