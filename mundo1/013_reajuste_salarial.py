"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salario = float(input('Qual é o salário atual do funcionário? R$'))
novo = (salario*15/100) + salario

print('Com o aumento de 15%, o salário do funcionário passa a ser de R${:.2f}'.format(novo))
