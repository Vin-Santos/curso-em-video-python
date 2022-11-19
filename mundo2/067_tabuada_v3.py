"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, pra cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
contador = 0
while True:
    numero = int(input('Digite um número para ver a tabuada (negativo para encerrar): '))
    print('- ' * 38)
    if numero < 0:
        break
    else:
        contador +=1
    for c in range(1, 11):
        print(f'\033[36m{numero}  x  {c:2}  = \033[m \033[32m{numero * c:2}\033[m')
    print('- ' * 38)
print(f'Você viu a tabuade de {contador} números. Volte sempre.\n')
