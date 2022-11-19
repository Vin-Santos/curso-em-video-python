"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
continuar = 'S'
soma = quantia = media = maior = menor = 0

while continuar == 'S':
    numero = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    soma += numero
    quantia += 1
    media = soma / quantia
    if quantia == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    if continuar not in 'SN':
        print('Valor inválido, programa encerrado.\n')

if continuar == 'N':
    print(f'A média dos {quantia} números é {media:.2f}.')
    if maior == menor:
        print('Não tem valor menor ou maior, são iguais.')
    else:
        print(f'O número maior é {maior} e o menor é {menor}.\n')
