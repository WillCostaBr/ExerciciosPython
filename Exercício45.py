print('''
COMPUTADOR: Vamos jogar Pedra, Papel, Tesoura!
As regras são as seguintes:
- Papel vence Pedra e perde para Tesoura
- Pedra vence Tesoura e perde para Papel
- Tesoura vence Papel e perde para Pedra
''')

from time import sleep
from random import choice

print('''
COMPUTADOR: Vamos jogar Pedra, Papel, Tesoura!
As regras são as seguintes:
- Papel vence Pedra e perde para Tesoura
- Pedra vence Tesoura e perde para Papel
- Tesoura vence Papel e perde para Pedra
''')

jogador = str(input('Escolha entre PEDRA, PAPEL E TESOURA:\n')).lower()
lista = ['pedra','papel','tesoura']
computador = choice(lista)

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)


if jogador != 'pedra' and jogador != 'papel' and jogador != 'tesoura':
    print('OPÇÃO INVÁLIDA!Escolha entre PEDRA, PAPEL E TESOURA')
if jogador == 'pedra' and computador == 'tesoura':
    print('Escolhi {}'.format(computador))
    print('Você ganhou!')
elif jogador == 'pedra' and computador == 'papel':
    print('Escolhi {}'.format(computador))
    print('Você perdeu!')
elif jogador == 'papel' and computador == 'pedra':
    print('Escolhi {}'.format(computador))
    print('Você ganhou!')
elif jogador == 'papel' and computador == 'tesoura':
    print('Escolhi {}'.format(computador))
    print('Você perdeu!')
elif jogador == 'tesoura' and computador == 'papel':
    print('Escolhi {}'.format(computador))
    print('Você ganhou!')
elif jogador == 'tesoura' and computador == 'pedra':
    print('Escolhi {}'.format(computador))
    print('Você perdeu!')
elif jogador == computador:
    print('Escolhi {}'.format(computador))
    print('EMPATE!')