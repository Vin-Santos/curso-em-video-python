"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Considere: US$1,00 = R$3,27
"""
reais = float(input('Quantos reais você deseja transformar em Dólares? R$'))

print(' ')
print('Com R${:.2f} você pode comprar US${:.2f}'.format(reais, reais/3.27))
