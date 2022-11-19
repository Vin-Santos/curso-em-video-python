"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""
print('Vamos analisar o que você disser.')
frase = input('Diga algo:')

print('O tipo primitivo do valor é', type(frase))
print('É um número?', frase.isnumeric())
print('Tem somente espaços?', frase.isspace())
print('É tudo maiúsculo?', frase.isupper())
print('É alfabético?', frase.isalpha())
print('É alfanumérico?', frase.isalnum())
print('É numérico?', frase.isnumeric())
print('Está em maiúsculo?', frase.isupper())
print('Está em minúsculo?', frase.islower())
print('Está capitalizado?', frase.istitle())
