"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.
"""
print('=~'*28)
print('{:^54}'.format('Adicione 5 números inteiros pelo teclado'))
print('{:^54}'.format('O programa mostrará o maior, o menor e suas posições'))
print('=~'*28)

# Adiciona 5 números digitados à lista
lista_numeros = []
for c in range(1, 6):
    numero = int(input(f'Digite o {c}º número: '))
    lista_numeros.append(numero)
maior = max(lista_numeros)
menor = min(lista_numeros)

# Cria listas para pôr as posições do maior e menor, e adiciona as posições nas listas usando for
posicoes_maior = []
posicoes_menor = []
for posicao, numero in enumerate(lista_numeros):
    if numero == maior:
        posicoes_maior.append(posicao + 1)
    if numero == menor:
        posicoes_menor.append(posicao + 1)

# Tranforma lista em string e remove colchetes, apenas para melhorar o visual no print
posicoes_maior = str(posicoes_maior).strip('[]')
posicoes_menor = str(posicoes_menor).strip('[]')

print('=~'*28)
print(f'A lista final é: {lista_numeros}')
print(f'O valor {maior} aparece nas posições {posicoes_maior}, é o maior de todos.')
print(f'Já o menor valor foi {menor}, aparecendo nas posições {posicoes_menor}.')
print('=~'*28)
