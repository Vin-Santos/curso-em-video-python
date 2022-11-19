"""
Crie um programa que leia o nome de uma pessoa e mostre na tela:
- O nome com todas as letras maiúsculas e minúsculas;
- Quantas letras ao todo (sem considerar espaços);
- Quantas letras tem o primeiro nome.
"""

print ('Análise de nomes')
nome = str(input('Digite seu nome completo: ')).strip()
maiusculo = nome.upper()
minusculo = nome.lower()
letras = len (''.join(nome.split()))
primeiro = (nome.split())[0]
letras_primeiro = len ((nome.split())[0])

print('Seu nome em maiúsculo é {}.'.format(maiusculo))
print('Seu nome em minúsculo é {}.'.format(minusculo))
print('Seu nome tem {} letas no total.'.format(letras))
print('Seu primeiro nome é {} e tem {} letras.'.format(primeiro,letras_primeiro))
