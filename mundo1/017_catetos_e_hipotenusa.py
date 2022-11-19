"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""
oposto = float(input('Digite o comprimento do cateto oposto:'))
adjacente = float(input('Digete o comprimento do cateto adjacente:'))
hipotenusa = (oposto**2 + adjacente**2) ** (1/2)

print ('O comprimento da hipotenusa de um triângulo retângulo com cateto oposto medindo {:.2f} e adjacente medindo {:.2f} é {:.2f}'.format(oposto, adjacente, hipotenusa))
