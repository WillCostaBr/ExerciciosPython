#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número e direi se é par ou ímpar: '))
if n % 2 == 0:
    print('{} é \033[34mPAR'.format(n))
else:
    print('{} é \033[35mÍMPAR'.format(n))