'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 25 anos: SÊNIOR
- Acima: MASTER'''

from datetime import date

nasc = int(input('Digite o ano de nascimento: '))

atual = date.today().year
idade = atual - nasc

print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif idade > 9 and idade <= 14:
    print('Sua categoria é INFANTIL.')
elif idade > 14 and idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade > 19 and idade <= 25:
    print('Sua categoria é SÊNIOR')
elif idade > 25:
    print('Sua categoria é MASTER')