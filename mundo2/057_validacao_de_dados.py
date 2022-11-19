"""
Faça um valor que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
genero = str(input('Qual seu gênero? [M/F]')).strip().upper()[0]
while genero not in 'MF':
    genero = str(input('Erro. Gênero não indentificado, digite novamento: ')).strip().upper()[0]
if genero == 'M':
    genero = 'Masculino'
else:
    genero = 'Feminino'
print(f'Seu gênero foi cadastrado como {genero}.')
