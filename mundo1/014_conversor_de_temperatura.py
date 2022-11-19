"""
Escreva um programa que converta uma temperatura digitada em ºC para ºF.
"""
celsius = float(input('Informe os graus em °C:'))
fahrenheit = ((9 * celsius) / 5) + 32

print('A temperatura de {}°C corresponde a {}°F!'.format(celsius, fahrenheit))
