'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros;
o primeiro que indique o número a calcular e o outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.'''

def fatorial(n=1, show=True):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


print(fatorial(5, show=True))