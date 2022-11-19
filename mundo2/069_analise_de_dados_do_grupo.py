"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deve perguntar se o usuário quer ou não continuar. No final, mostre:
- Quantas pessoas têm mais de 18 anos;
- Quantos homens foram cadastrados;
- Quantas mulheres têm menos de 20 anos.
"""
mais_dezoito = homens_na_lista = mulheres_menos_vinte = 0

while True:
    print('-'*26)
    print('   CADASTRE UMA PESSOA')
    print('-'*26)
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    print('-'*26)
    if idade >= 18:
        mais_dezoito += 1
    if sexo == "M":
        homens_na_lista += 1
    if sexo == "F" and idade < 20:
        mulheres_menos_vinte +=1

    continuar = ' '
    while continuar not in 'SN':
        continuar = input("Deseja continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        break
print('-'*26)
print(f"""No total, o número de pessoas com mais de 18 anos é {mais_dezoito};
O número de homens citados foi {homens_na_lista};
O número de mulheres com menos de 20 anos é {mulheres_menos_vinte}.""")

