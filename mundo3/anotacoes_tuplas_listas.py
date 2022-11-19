

print(' \n ANOTAÇÕES SOBRE TUPLAS \n ')


lanche = ('hamburguer', 'suco', 'pizza', 'pudin', 'banana')
print(lanche[2]) # Mostra pizza
print(lanche[0:2]) # Mostra hamburguer e suco
print(lanche[1:]) # Mostra do suco ao pudim
print(lanche[-1]) # Mostra pudim
print(sorted(lanche)) # Mostra em ordem
print(len(lanche)) # Mostra quantos termos tem a Tupla
# del(lanche) # Deleta a Tupla completa, mas não consegue apagar só um elemento.
# lanche[1] = 'refrigerante' # !!! Vai dar erro !!!  Tuplas são imutáveis

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.count(2)) # Quantas vezes aparece tal elemento
print(c.index(8)) # Mostra a posição do elemento
print(c.index(5, 1)) # Mostra a posição do elemento, começando a contar pelo 1, ou seja, vai ver onde tem '5' mas pulando todas as posições antes do 1. O primeiro parametro é o número que você quer saber a posição e o segundo é a partir de qual posição vai começar a contar.

for comida in lanche:
    print(f'Eu vou comer {comida}')

for c in range(len(lanche)): # Len() conta os itens
    print(f'Eu vou comer {lanche[c]}')

for posicao, comida in enumerate(lanche): #Dá o dado e a posição
    print(f'Eu vou comer {comida}, na posição {posicao}')


print(' \n ANOTAÇÕES SOBRE LISTAS \n ')


numeros = [2, 5, 9, 1]
print(numeros)
numeros[2] = 3  # Podemos mudar os itens da list atribuindo novos valores
print(numeros)
numeros.append(7)  # Adiciona um número no fim da lista (nesse caso, 7)
print(numeros)
numeros.insert(2, 7) #  Adiciona o número 7 e coloca na posição 2, empurrandos os outros pra frente
print(numeros)
numeros.pop(0) #  Apaga o elemento na posição 0, apaga o último se não escolher um 
print(numeros)
numeros.remove(7) #  Apaga o elemento 7 na lista (somenta a primeira aparição)
print(numeros)
numeros.sort(reverse=True)  # Coloca a lista em ordem. 'reverse=True' para ficar invertido
print(numeros)
print(len(numeros))  # Conta quantos elementos tem a lista

novos_numeros = numeros #  Cria ligação entre as listas, se mudar uma, muda a outra
novos_numeros = numeros[:] #  Copia todos os valores de uma lista para uma outra, atribuindo-os
