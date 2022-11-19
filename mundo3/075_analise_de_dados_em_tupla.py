"""
Desenvolva um programa que leia quatro valor pelo teclado e guarde-os em uma tupla. No final, mostre:
- Quantas vezes apareceu o valor 9;
- Em que posição foi digitado o primeiro valor 3;
- Quais foram os números pares.
"""

print('=~'*12)
print('Escolha quatro números')
print('=~'*12)
numeros = (int(input('Digite o primerio: ')), int(input('Agora digite o segundo: ')), int(input('Esse será o terceiro: ')), int(input('E por fim o quarto: ')))

print('=~'*12)
print(f'Analisando os números: {numeros}')
print(f'O número de vezes que o nove aparece é {numeros.count(9)}.')

if 3 in numeros:
    print(f'O número três aparece pela primeira vez na posição {numeros.index(3)+1}.')
else:
    print('O número três não aparece.')

print(f'Os pares são:', end=' ')
for pares in numeros:
    if pares % 2 == 0:
        print(pares, end=' ')
