'''Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
Depois disso mostre a listagem de números gerados e também indique o menor e o maior valor
que estão na tupla'''

import random

tupla = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10),
random.randint(0,10))
print(f'Os valores sorteados foram: ', end='')
for n in tupla:
    print(f'{n} ', end='')

print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')