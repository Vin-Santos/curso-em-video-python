"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
from random import choice 
aluno1 = input('Primeiro aluno:')
aluno2 = input('Sugundo aluno:')
aluno3 = input('Terciro aluno:')
aluno4 = input('Quarto aluno:')
lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = choice(lista)
print ('O aluno escolhido foi', escolhido)
