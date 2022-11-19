"""
Escreva um programa que leia um valor em mentros e o exiba convertido em centímetros e milímetros.
"""
metros = float(input('Digite uma distância em metros:'))
centimetros = metros * 100
milimetros = metros * 1000

print("{} metros são {} centímetros e {} milímetros".format(metros, centimetros, milimetros))
