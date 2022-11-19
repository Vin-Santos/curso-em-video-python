"""
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
"""
from time import sleep

print('\033[34m-=- \033[m' * 6)
print('\033[34mProgressão Aritimética\033[m')
print('\033[34m-=- \033[m' * 6)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão para seguir: '))
parar = 0
contador = 0

while parar < 10:
    print(f'{primeiro}', end='  ')
    primeiro += razao
    parar +=1
    contador += 1
nova_quantia = int(input('\nDeseja ver mais qunatos termos? '))
while nova_quantia > 0:
    for _ in range(0, nova_quantia):
        print(f'{primeiro}', end='  ')
        primeiro += razao
        contador += 1
    nova_quantia = int(input('\nDeseja ver mais qunatos termos? '))
if nova_quantia < 0:
    print('Quantia inválida. Encerrando...')
    sleep(1)
else:
    sleep(1)
print('FIM!')
print(f'Você viu {contador} termos da PA.')
