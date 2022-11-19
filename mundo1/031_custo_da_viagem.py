"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
"""
distancia = float(input('Qual a distância da sua viagem? '))
if distancia < 200:
    print(f'O valor da sua viagem será de R${distancia * 0.50:.2f}')
else:
    print (f'O valor da sua viagem será de R${distancia * 0.45:.2f}')
print('Tenha uma boa viagem.')
