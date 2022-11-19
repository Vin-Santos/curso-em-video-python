"""
Crie um programa que tenha uma tupla única com nome de produtose seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
comidas = ('Hamburguer', 12.50, 
           'Batata frita', 6.00, 
           'Misto quente', 7.80, 
           'Cachorro quente', 10, 
           'A la minuta', 20.90, 
           'Acarajé', 9.50, 
           'Pão de queijo', 7.69, 
           'Arroz carreteiro', 9.99)

print('-'*48)
print('{:^48}'.format('C O M I D A S'))
print('-'*48)
comida = 0
while comida < len(comidas):
    print(f'{comidas[comida]:.<40}R$', end='')
    comida += 1
    print(f'{comidas[comida]:>7.2f}')
    comida += 1
print('-'*48)
