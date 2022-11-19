"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
- Quantos números foram digitados.
- A lista de valores, ordenada de forma decrescente.
- Se o valor 5 foi digitado e está ou não na lista.
"""

lista_numeros = []
quantidade = 1
print('~='*20)

continuar = ''
while continuar != 'N':
    lista_numeros.append(int(input(f'\033[33mDigite o {quantidade}º número:\033[m ')))
    while continuar != 'N':
        continuar = input('\033[35mDeseja adicionar outro? [S/N]\033[m ').upper().strip()[0]
        if continuar == 'S':
            quantidade += 1
            break
    print('~='*20)

lista_numeros.sort(reverse=True)
print(f'\033[32mNo total, foram armazenados {quantidade} números na lista.\033[m')
print(f'\033[32mOs números digitados, em ordem decrescente, são: {lista_numeros}\033[m')
if 5 in lista_numeros:
    print(f'\033[32mO número 5 foi digitado e está na lista.\033[m')
else:
    print(f'\033[32mO número 5 não foi digitado e não está na lista.\033[m')
