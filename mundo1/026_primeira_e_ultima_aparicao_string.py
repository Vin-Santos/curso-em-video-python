"""
Faça um programa que leia uma frase pelo teclado e mostre na tela:
- Quantas vezes aparece a letra "A";
- Em que posição ela aparece a primeira vez;
- Em que posição ela aparece a última vez.
"""
frase = str(input('Digite uma frase: ')).lower().strip()
vezes = frase.count('a')
primeira = frase.find('a')+1
ultima = frase.rfind('a')+1
print (f'A letra a aparece {vezes} vezes.')
print (f'A letra a apapare primeiro na posição {primeira}.')
print (f'A latra a aparece por último na posição {ultima}.')
