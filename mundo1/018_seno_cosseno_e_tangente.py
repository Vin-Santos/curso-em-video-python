"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.
"""
from math import sin,cos,tan, radians
angulo = int(input('Digite um ângulo:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo de {}° tem seno {:.2f}, cosseno {:.2f} e tangente {:.2f}!'.format(angulo,seno,cosseno,tangente))
