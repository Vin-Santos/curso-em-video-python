"""
Crie um programa onde o usuário possa digitar vários valores numéricos, e cadastre-os em uma lista. Caso o múmero já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

print('~='*18)
print('Digite quantos números você desejar')
print('No final, os verá em ordem crescente')
print('Os números repetidos serão ignorados')
print('~='*18)
continuar = ''
lista_numeros = []
while continuar != 'N':
    numero = int(input('Digite o número que deseja: '))
    if numero not in lista_numeros:
        lista_numeros.append(numero)
    while continuar != 'N':
        continuar = input('Deseja continuar? [S/N]').upper().strip()[0]
        if continuar == 'S':
            break
    print('~='*18)

lista_numeros.sort()
print(f'Os números digitados, em ordem crescente, forão: {lista_numeros}')
