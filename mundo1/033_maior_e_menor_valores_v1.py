"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
print(f'Os números escolhidos foram {numero1}, {numero2} e {numero3}.')

if numero1 > numero2 and numero1 > numero3:
    print (f'O maior deles é {numero1}.')
if numero2 > numero1 and numero2 > numero3:
    print (f'O maior deles é {numero2}.')
if numero3 > numero1 and numero3 > numero2:
    print (f'O maior deles é {numero3}')
if numero1 < numero2 and numero1 < numero3:
    print (f'O menor deles é {numero1}.')
if numero2 < numero1 and numero2 < numero3:
    print (f'O menor deles é {numero2}.')
if numero3 < numero1 and numero3 < numero2:
    print (f'O menor deles é {numero3}.')

# ...ou podemos considerar um número como o maior e testar os outros, depois considerar o mesmo número como o menor e testar os outros, foi assim que o professor fez no vídeo de correção.
