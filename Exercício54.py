''' Crie um programa que leia o ano de nascimento de sete pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''

from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    ano = int(input('Digite o ano de nascimento a {}ª pessoa: '.format(c)))
    idade = atual - ano
    if idade <= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Existem {} pessoas maiores de idade'.format(totmaior))
print('E também há {} pessoas menores de idade'.format(totmenor))