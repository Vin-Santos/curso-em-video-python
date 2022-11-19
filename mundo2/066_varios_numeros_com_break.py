"""
Crie um programa que leia vários números interos pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. (desconsiderando o flag, 999)
Esse exercício é igual ao 064, porém melhorado, usando 'break'
"""

contador = soma = 0
while True:
    numero = int(input('Digite números para serem somados [999 para parar]: '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'A soma dos {contador} números digitados foi {soma}.\n')
