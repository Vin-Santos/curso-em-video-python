"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior;
- O segundo valor é maior;
- Naão exite valor maior, os dois são iguais.
"""
primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))

if primeiro > segundo:
    print (f'O maior valor é o primeiro, o número \033[4;31m{primeiro}\033[m.')
elif segundo > primeiro:
    print (f'O maior valor é o segundo, o número \033[4;31m{segundo}\033[m.')
else:
    print ('Não existe valor maior, os dois são iguais.')
