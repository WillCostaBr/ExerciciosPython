'''Crie um programa que vai ler vários números
e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas
os valores pares e o valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

a = list()
b = list()
c = list()

while True:
    n = int(input('Digite um valor: '))
    a.append(n)
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
    if n % 2 == 0:
        b.append(n)
    elif n % 2 == 1:
        c.append(n)
    
print(f'A lista completa é {a}')
print(f'A lista de pares é {b}')
print(f'A lista de ímpares é {c}')