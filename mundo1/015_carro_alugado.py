"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
"""
quilometros = int(input('Quantos quilometros o seu carro alugado percorreu?'))
dias = float(input('Por quatos dias você alugou o carro?'))

preco_km = 0.15 * quilometros
preco_dias = 60 * dias
total = preco_km + preco_dias

print('O preço a se pagar por {}km rodados são R${:.2f}, e por {} dias de uso são R${:.2f}. \nO valor total que deve ser pago são R${:.2f}'. format(quilometros, preco_km, dias, preco_dias, total))
