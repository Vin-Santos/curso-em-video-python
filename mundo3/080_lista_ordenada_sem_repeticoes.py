"""
Crie um prorama onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta da inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
lista_numeros = []

print('~='*22)
for contador in range(5):
    numero = int(input('Digite um número: '))

    if contador == 0:
        lista_numeros.append(numero)
        print(f'O número {numero} foi adicionado no fim da lista.')
    elif contador == 1:
        if numero > lista_numeros[0]:
            lista_numeros.append(numero)
            print(f'O número {numero} foi adicionado no fim da lista.')
        else:
            lista_numeros.insert(0, numero)
            print(f'O número {numero} foi adicionado na posição 0.')
    elif contador > 1:
        posicao = 0
        while numero > lista_numeros[posicao]:
            posicao += 1
            if posicao == len(lista_numeros):
                break
        if posicao == len(lista_numeros):
            lista_numeros.append(numero)
            print(f'O número {numero} foi adicionado no fim da lista.')
        else:    
            lista_numeros.insert(posicao, numero)
            print(f'O número {numero} foi adicionado na posição {posicao}.')
    print('~='*22)

print(f'A lista ficou ordenada da seguinte forma: {lista_numeros}')
