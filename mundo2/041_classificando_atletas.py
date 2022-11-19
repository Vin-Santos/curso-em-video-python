"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: mirim;
- Até 14 anos: infantil;
- Até 19 anos: junior;
- Até 25 anos: sênior;
- Acima disso: master.
"""
from datetime import date

ano = int(input('Insira o ano de nascimento do atleta: '))
idade = date.today().year - ano
print(f'O atleta nascido em {ano} tem {idade} anos')

if idade <= 9:
    print('Pertence à categoria MIRIM ')
elif idade <= 14:
    print('Pertence à categoria INFANTIL')
elif idade <= 19:
    print('Pertence à categoria JUNIOR')
elif idade <= 20:
    print('Perteence à categoria SÊNIOR')
elif idade > 20:
    print('Pertence à categoria MASTER')

