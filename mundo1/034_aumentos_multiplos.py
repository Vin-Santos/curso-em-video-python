"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
- Para salários superiores a R$1.250,00: Calcule aumento de 10%.
- Para os inferiores ou iguais: Calcule um aumento de 15%.
"""

print ('Digite seu salário a seguir para verificar seu aumento.')
salario = float(input('Salário atual: R$'))

if salario > 1250:
    aumento = '10%'
    atual = ((10 / 100) * salario) + salario
else:
    aumento = '15%'
    atual = ((15 / 100) * salario) + salario
print (f'Você recebeu um aumento de {aumento}, seu salário atual é R${atual:.2f}.')
