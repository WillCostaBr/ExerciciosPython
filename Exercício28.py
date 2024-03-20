# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 epeça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador. O computador deverá escrever se o usuário ganhou ou perdeu

#from random import choice
#num = int(input('Escolha um número entre 0 e 5: '))

#lista = [0,1,2,3,4,5]
#pc = choice(lista)

#if num == pc:
    #print('Número do computador: {}\nSeu número: {}'.format(pc,num))
    #print('Você adivinhou o número.PARABÉNS!!')
#else:
    #print('Número do computador: {}\nSeu número: {}'.format(pc,num))
    #print('Você não advinhou o número.BOA SORTE NA PRÓXIMA!!')

from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('\033[34mVou pensar em um número ENTRE 0 E 5.TENTE ADIVINHAR!\033[m')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('\033[1;32;40mPARABÉNS!! VOCÊ ACERTOU!!\033[m')
else:
    print('\033[31mERROU!! O número que pensei foi \033[1m{}\033[m\033[31m e não \033[1;31m{}\033[m'.format(computador,jogador))
