'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

nascimento = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year

idade = atual - nascimento

'''print('Você tem {} anos'.format(idade))
if idade < 18:
    print('Você ainda não tem idade suficiente para se alistar')
elif idade == 18:
    print('Você precisa se alistar esse ano!')
else:
    print('Já passou da idade de se alistar.')'''

print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))



