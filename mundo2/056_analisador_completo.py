"""
Desenvolva um programa que leia o nome a idade e o sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo;
- Qual é o nome do homem mais velho;
- Quantas mulheres têm menos de 20 anos.
"""

media_idade = 0
idade_mais_velho = 0
nome_mais_velho = ''
total_mulheres = 0

for pessoa in range(1, 5):
    print(f'\033[34m{pessoa:^3}º  P e s s o a\033[m')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M ou F]: ')).strip().upper()[0]
    media_idade += (idade / 4)
    if sexo == 'M' and idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome
    if sexo == 'F' and idade < 20:
        total_mulheres += 1

print(f'\033[34m-\033[m'*18)
if nome_mais_velho == '':
    print('Não ha nenhum homem entres as pessoas.')
else:
    print(f'O homem mais velho se chama {nome_mais_velho}, com {idade_mais_velho}')
print(f'O total de mulheres acima de 20 anos é {total_mulheres}')
print(f'A média de idade do grupo é de {media_idade} anos.')
