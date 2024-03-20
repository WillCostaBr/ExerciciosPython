''' Crie um programa que leia dois valores e mostre um menu
na tela:

1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa

Seu programa deverá realizar a operação solicitada em cada caso '''

from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
menu = 0

while menu != 5:
    sleep(2)
    print('-=-' * 10)
    print('''          Menu''')
    print('-=-' * 10)
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior Valor
    [ 4 ] Novos números
    [ 5 ] Sair''')
    menu = int(input('Qual a opção desejada? '))
    sleep(2)
    if menu == 1:
        somar = n1 + n2
        print('{} + {} é igual a {}'.format(n1, n2, somar))
    elif menu == 2:
        multiplicar = n1 * n2
        print('{} x {} é igual a {}'.format(n1, n2,multiplicar))
    elif menu == 3:
        if n1 > n2:
            maior = n1
            print('O maior número é {}'.format(maior))
        elif n2 > n1:
            maior = n2
            print('O maior número é {}'.format(maior))
        else:
            print('Os números são iguais')
    elif menu == 4:
        print('Informe os novos valores')
        n1 = int(input('Digite um novo valor: '))
        n2 = int(input('Digite outro valor: '))
    elif menu == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Dados inválidos!')