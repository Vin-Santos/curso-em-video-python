"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é hora de se alistar, ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

nascimento = int(input('\033[33mInforme seu ano de nascimento:\033[m '))
atual = date.today().year
idade = atual - nascimento

# Condição de quando deveria/deve/deverá se alistar
if idade < 18:
    print(f'Você tem {idade} anos. Deverá se alistar', end=' ')
elif idade == 18:
    print(f'Você tem {idade} anos. Deve se alistar', end=' ')
elif idade > 18:
    print(f'Você tem {idade} anos. Deveria se alistar', end=' ')

# Quanto tempo falta / quanto tempo passou do prazo
if idade < 18:
    tempo = 18 - idade
    ano = nascimento + 18
    print(f'daqui a {tempo} anos, em {ano}!')
elif idade == 18:
    print('o quanto antes!')
elif idade > 18:
    tempo = idade - 18
    ano = nascimento + 18
    print(f'há {tempo} anos, em {ano}!')
