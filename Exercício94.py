'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres
d) Uma lista com todas as pessoas com idade cima da média'''

galera = list()
pessoas = dict()

cont = 0
media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] '))
    pessoas['idade'] = int(input('Idade: '))
    cont += 1
    galera.append(pessoas.copy())
    media += pessoas['idade']
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break

media = media /cont
print('-='*30)
print(f' - O grupo tem {cont} pessoas.')
print(f' - A média de idade é de {media} anos.')

'''for i, v in enumerate(pessoas)
    print(f' - As mulheres cadastradas foram: {}')'''
print(pessoas)