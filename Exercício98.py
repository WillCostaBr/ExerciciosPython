'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

#Minha solução...
'''from time import sleep

print('-='*40)
print('Contagem de 1 até 10 de 1 em 1')
for c in range(1, 11, 1):
    print(f'{c} ', end='')
    sleep(0.5)
print('FIM!')

print('-='*40)
print('Contagem de 10 até 0 de 2 em 2')
for c in range(10, -1, -2):
    print(f'{c} ',end='')
    sleep(0.5)
print('FIM!')
print('-='*40)

print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
for c in range(inicio, fim+1, passo):
    print(f'{c} ', end='')
    sleep(0.5)
print('FIM!')'''

from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*40)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
    print('FIM!')

#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)