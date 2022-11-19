"""
Faça um programa que leia a largura e altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la. Sabendo que cada litro de tinta pinta 2m².
"""
largura = float(input('Qual a largura da sua parede (em metros)?'))
altura = float(input('Qual a altura da sua parede (em metros)?'))

area = altura * largura
litros = area / 2

print('Para pintar toda sua parede você precisará de {:.1f} litro de tinta.'.format(litros))
