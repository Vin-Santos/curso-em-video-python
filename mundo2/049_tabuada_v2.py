"""
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, se que agora utilizando um laço for.
"""
numero = int(input('\033[33mDigite um número e veja a tabuada:\033[m '))
print('-' * 13)
for tabuada in range(1, 11):
    print(f'{numero} x {tabuada:2} = {numero * tabuada:2}')
print('-' * 13)
