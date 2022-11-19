"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
- À vista em dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
print('- - ' * 8)

preco = float(input('Qual o preço do produto? R$'))
print('Digite \033[34m[1]\033[m para pagamento à vista no dinheiro ou cheque.\n'
      'Digite \033[34m[2]\033[m para pagamento à vista no cartão\n'
      'Digite \033[34m[3]\033[m se forem 2x no cartão\n'
      'Digite \033[34m[4]\033[m se for 3x ou mais no cartão')
condicao = int(input('Digite sua forma de pagamento: '))

if condicao == 1:
    desconto = (10 / 100) * preco
    novopreco = preco - desconto
    print(f'Desconto de R${desconto}. O novo preço é R${novopreco}')
elif condicao == 2:
    desconto = (5 / 100) * preco
    novopreco = preco - desconto
    print(f'Desconto de R${desconto}. O novo preço é R${novopreco}')
elif condicao == 3:
    print('Você pagará o valor normal do produto')
elif condicao == 4:
    juros = (20 / 100) * preco
    novopreco = preco + juros
    print(f'R${juros} de juros. O novo preço é de {novopreco}')
