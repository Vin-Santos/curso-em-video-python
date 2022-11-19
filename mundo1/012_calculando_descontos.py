"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
antigo = float(input('Qual é o preço do produto? R$'))
desconto = 5 / 100 * antigo
atual = antigo - desconto

print('O produto recebeu um desconto de R${:.2f}'.format(desconto))
print('Atualmente custa R${:.2f}'.format(atual))
