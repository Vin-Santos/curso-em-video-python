"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seus status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- De 25 até 30: Sobrepeso
- De 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""
print('\033[34m+ + \033[m' * 5)
print('\033[34mCalculadora de IMC\033[m')
print('\033[34m+ + \033[m' * 5)

peso = float(input('\n\033[33mDigite seu peso: (Kg)\033[m'))
altura = float(input('\033[33mDigite sua altura: (m)\033[m'))
IMC = peso / (altura**2)
print(f'Com peso de \033[36m{peso:.2f}\033[m e altura \033[36m{altura:.2f}\033[m'
      f' o IMC é de \033[36m{IMC:.1f}\033[m')

if IMC < 18.5:
    print('Você está \033[36mABAIXO DO PESO IDEAL!\033[m')
elif 18.5 <= IMC < 25:
    print('Você está no \033[36mPESO IDEAL!\033[m')
elif 25 <= IMC < 30:
    print('Você está com \033[36mSOBREPESO!\033[m')
elif 30 <= IMC < 40:
    print('Você tem \033[36mOBESIDADE!\033[m')
elif 40 <= IMC:
    print('Você tem \033[36mOBESIDADE MÓRBIDA!\033[m')
