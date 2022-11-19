"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
numero = int(input('Escolha um número:'))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print('O dobro de', numero,'é {}, \nO triplo é {}, \nE a raiz quadrada é {:.2f}!'.format(dobro, triplo, raiz))
