"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. (desconsiderando o flag, 999)
"""

numeros = contador = soma_dos_numeros = 0

while numeros != 999:
    numeros = int(input('Digite os números para somar [999 para parar]: '))
    if numeros != 999:
        soma_dos_numeros += numeros
        contador += 1
print(f'A soma dos {contador} números digitados é {soma_dos_numeros}.')
