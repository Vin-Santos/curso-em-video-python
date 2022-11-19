"""
Crie um programa que leia duas notas de um aluno e calcule sua méida, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Méida entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""

# Ler as duas notas do aluno + estipular média
nota1 = float(input('\033[33mDigite sua primeira nota:\033[m '))
nota2 = float(input('\033[33mDigite sua segunda nota:\033[m '))
media = (nota1 + nota2) / 2

# Informar se está aprovado, reprovado ou em recuperação
if media <= 5.0:
    print(f'\033[31mREPROOVADO!\033[m Sua média foi {media}. Estude mais ano que vem!')
elif 5.0 < media <= 6.9:
    print(f'\033[34mRECUPERAÇÃO!\033[m Sua média foi {media}. Estude um pouco mais para passar de ano!')
elif media >= 7.0:
    print(f'\033[32mAPROVADO!\033[m Sua média foi {media}. Parabéns pelo esforço!')
