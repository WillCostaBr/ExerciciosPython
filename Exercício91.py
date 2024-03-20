'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
em um diconário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado'''

from time import sleep
from random import randint
from operator import itemgetter

cont = 0
dado = {"Jogador1": randint(1,6),
        "Jogador2": randint(1,6),
        "Jogador3": randint(1,6),
        "Jogador4": randint(1,6)}

ranking = list()
print("Valores Sorteados:")
for k, v in dado.items():
        print(f'{k} tirou {v} no dado.')
        sleep(1)

print('-='*30)

print('  == RANKING DOS JOGADORES ==')
sleep(1)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
        print(f'  {i+1}º lugar: {v[0]} com {v[1]}')
        cont += 1
        sleep(1)
print(f'{ranking[0][0]} ganhou!!!')

