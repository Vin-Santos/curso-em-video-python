"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""
print('- -' * 12)
print('Análise de empréstismo bancário')
print('- -' * 12)

custo = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual seu salário menasl? R$'))
anos = int(input('Vai pagar em quantos anos? '))
prestacao = custo / (anos * 12)

if prestacao >= (30 / 100) * salario:
    print('Infelizmente você NÃO PODERÁ financiar essa casa.')
else:
    print(f'A prestação mensal a ser paga é de R${prestacao}')
