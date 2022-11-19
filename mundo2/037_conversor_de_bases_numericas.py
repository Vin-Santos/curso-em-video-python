"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário; 2 para octal; 3 para hexadecimal.
"""

numero = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
escolha = int(input('Sua escolha: '))

if escolha == 1:
    print(f'Convertido para BINÁRIO é igual a {bin(numero)[2:]}')
elif escolha == 2:
    print(f'Convertido para OCTAL é igual a {oct(numero)[2:]}')
elif escolha == 3:
    print(f'Convertido para HEXADECIMAL é igual a {hex(numero)[2:]} ')
else:
    print('Opção inválida. Encerrando...')
