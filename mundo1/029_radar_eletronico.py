"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""
print ('- '*19)
velocidade = float(input('O carro percorre a quantos Km/h? '))
if velocidade > 80:
    print (f'Você ultrapassou o limite de 80km/h.')
    print (f'Deverá pagar uma multa de R${(velocidade - 80)* 7:.2f}!')
else:
    print ('Você está dentro do limite de velocidade.\nTenha um bom dia.')
print ('- '*19)
