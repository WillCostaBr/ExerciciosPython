'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep
def contador(*num):
    cont = maior = 0
    print('-='*40)
    print(f'Analisando os valores passados...')
    sleep(1)
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#Programa Principal:
contador(2,9,4,5,7,1)
contador(4,7,0)
contador(1,2)
contador(6)
contador()