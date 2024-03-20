'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores pares sorteados pela função anterior.'''

from random import randint
from time import sleep

'''def lista(*num):
    print('Sorteando 5 valores da lista: ')
    cont = 0
    soma = 0
    for c in num:
        print(f'{c} ', end='')
        cont += 1
        sleep(0.5)
        if c % 2 == 0:
            soma += c
    print('PRONTO!')
    print(f"Somando os valores pares de {num}, ", end='')
    print(f'{soma}')

lista(randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))'''

def sorteia():
    print('Sorteando 5 valores da lista: ')
    for c in numeros:
        print(f'{c} ', end='')
        sleep(0.5)
    print('PRONTO!')

def somapar():
    sleep(1)
    print(f'Somando os valores pares de {numeros}, ', end='')
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'temos {soma}')

numeros = [randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)]
sorteia()
somapar()