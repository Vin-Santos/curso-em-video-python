"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos), depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('banana', 'batedeira', 'mesa', 'chiclete',
            'caneta', 'cultura', 'conhecimento', 'kiwi')
vogais = 'aeiou'

for palavra in palavras:
    print(f'\nAs vogais da palavra {palavra} são: ', end=' ')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')
