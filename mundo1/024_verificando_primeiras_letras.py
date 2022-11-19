"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo".
"""
cidade = str(input('Qual cidade você nasceu? ')).strip().lower()
print ('Sua cidade começa com Santo? {}'.format(cidade[0:5] == 'santo'))
