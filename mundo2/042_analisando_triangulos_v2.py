"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: Todos os lados iguais. 
- Isósceles: Dois lados iguias.
- Escaleno: Todos os lados diferentes.
"""
print('\033[34m- -\033[m' * 11)
print('\033[34mAnálise da formção de triângulos\033[m')
print('\033[34m- -\033[m' * 11)

p = float(input('\033[33mPrimeira reta: \033[m'))
s = float(input('\033[33mSegunda reta: \033[m'))
t = float(input('\033[33mTerceira reta: \033[m'))

if s-t <p< s+t and p-t <s< p+t and p-s <t< p+s:
    print('\033[32mAs retas podem formar um triângulo\033[m', end=' ')
    if p == s == t:
        print('\033[32mequilátero!\033[m')
    elif p == s != t or s == t != p or t == p != s:
        print('\033[32misósceles!\033[m')
    elif p != s != t != p:
        print('\033[32mescaleno!\033[m')
else:
    print('\033[31mAs retas NÃO podem formar um triângulo.\033[m')
