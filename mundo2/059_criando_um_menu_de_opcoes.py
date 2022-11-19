"""
Crie um programa que leia dois valores e mostre um menu, seguindo o exemplo abaixo:
[ 1 ] Somar      
[ 2 ] Multiplicar
[ 3 ] Ver o maior
[ 4 ] Digitar novos números
[ 5 ] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep
primeiro = int(input('\nDigite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))

while True:
    sleep(1)
    print('\n\033[34m[ 1 ]\033[m \033[33mSomar\033[m\n'
'\033[34m[ 2 ]\033[m \033[33mMultiplicar\033[m\n'
'\033[34m[ 3 ]\033[m \033[33mVer o maior\033[m\n'
'\033[34m[ 4 ]\033[m \033[33mDigitar novos números\033[m\n'
'\033[34m[ 5 ]\033[m \033[33mSair do programa\033[m\n')
    escolha = int(input('Qual opção você deseja? '))

    if escolha == 1:
        print(f'Somando {primeiro} + {segundo} resulta em {primeiro + segundo}.')
    elif escolha == 2:
        print(f'Multiplicando {primeiro} x {segundo} teremos {primeiro * segundo}.')
    elif escolha == 3:
        if primeiro > segundo:
            print(f'Entre os números {primeiro} e {segundo} o maior é {primeiro}.')
        elif segundo > primeiro:
            print(f'Entre os números {primeiro} e {segundo} o maior é {segundo}.')
        else:
            print('Os números são iguais.')
    elif escolha == 4:
        print('Quais serão os novos números?')
        sleep(0.5)
        primeiro = int(input('Digite o primeiro: '))
        segundo = int(input('Digite o segundo: '))
    elif escolha == 5:
        print('Encerrando o programa...')
        sleep(2)
        print('Obrigado por utilizar nossos serviços!\n')
        break
    else:
        print('\033[31mOpção inválida!\033[m')
