"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
- Qual é o total gasto na compra;
- Quantos produtos custam mais de R$1000;
- Qual é o nome do produto mais barato.
"""
total_gasto = mais_de_1000 = mais_barato = contador = 0

while True:
    print('-'*26)
    print('\033[32m   CADASTRO DE PRODUTOS\033[m')
    print('-'*26)
    nome = str(input('Nome do pruduto: '))
    preco = float(input('Preço: R$'))
    print('-'*26)
    total_gasto += preco

    if preco >= 1000:
        mais_de_1000 += 1
    contador += 1
    if contador == 1 or preco < mais_barato:
        mais_barato = preco
        produto = nome

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print('-'*26)
print('\033[32m    SOBRE OS PRODUTOS\033[m')
print('-'*26)
print(f'No total foi gasto R${total_gasto} reais.')
print(f'No total {mais_de_1000} produtos custaram mais de R$1000 reais')
print(f'E o produto mais barato foi o(a) {produto}')

