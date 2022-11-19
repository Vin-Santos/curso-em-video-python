"""
Crie um program que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""
from math import trunc
numero = float(input('Digite um número real para ver sua parte inteira:'))
inteiro = trunc(numero)

print('A parte inteira de {} é {}!'.format(numero, inteiro))

# Também pode-se usar a função int() assim como o professor fez no vídeo de correção, ao invés de importar trunc().
