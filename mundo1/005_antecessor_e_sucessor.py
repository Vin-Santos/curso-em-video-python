"""
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""
numero = int(input('Escolha um número:'))
antecessor = numero - 1
sucessor = numero + 1

print('Analisando o número {}, vemos que seu antecessor é {} e seu sucessor é {}!'.format(numero, antecessor, sucessor))
