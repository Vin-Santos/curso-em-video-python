"""
Crie uma tupla preenchida com os vinte primeiros colocados da Tabela do Campionato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
- Os 5 primeiros;
- Os últimos 4 colocados;
- Os times em ordem alfabética;
- Em que posição está o time da Chapecoense.
"""

brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Corinthians', 'Fluminense', 
'Atlético-PR', 'Atlético-MG', 'São Paulo', 'América-MG', 'Fortaleza', 'Botafogo', 'Santos', 
'Bragantino', 'Goiás', 'Curitiba', 'Ceará SC', 'Atlético-GO', 'Cuiabá', 'Avaí', 'Juventude')

print('\nAnalisando a tabela do Brasileirão em 2022, podemos constatar:')
print(f'\033[34mOs cinco primeiros colocados são:\033[m\n {brasileirao[:5]}')
print(f'\033[34mOs quatro últimos colocados são:\033[m\n {brasileirao[16:]}')
print(f'\033[34mEm ordem alfabética temos:\033[m\n {sorted(brasileirao)}')
print('\033[34mEm que posição está o time da Chapecoense:\033[m')
if 'Chapecoense' in brasileirao:
    print('O Chapecoense está na {}º posição.'.format(brasileirao.index('Chapecoense')+1))
else:
    print('A Chapecoense não está entre os 20 primeiros colocados.')

# Como vi que a Chapecoense não estava entre os 20 primeiros desse ano (2022), adicionei essa estrutura condicional que verifica se ela está ou não. Além disso, usei a o método de formatação .format(), pois a f-string estava dando erro quando eu usava com .index()
