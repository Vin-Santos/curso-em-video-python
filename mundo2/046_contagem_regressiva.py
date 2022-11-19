"""
Faça um programa que mostre na tela uma contagem regressiva na tela para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de um segundo até elas.
"""
import time
import emoji

for contagem in range(10, 0, -1):
    print(contagem)
    time.sleep(1)
print(contagem-1)
print(emoji.emojize('POOOW, POOOW, BOOW!!!!\U0001f386\U0001f386\U0001f386'))
