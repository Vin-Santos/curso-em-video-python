"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunsa reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r2-r3 < r1 < r2+r3 and r1-r3 < r2 < r1+r3 and r1-r2 < r3 < r1+r2:
    print('As três retas PODEM formar um rtiângulo!')
else:
    print('As três retas NÃO PODEM formar um triângulo!')
