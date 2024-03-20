'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final mostre:

a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves '''

pessoas = list()
cadastro = list()

maior = menor = 0

cont = 0

while True:
    cadastro.append(str(input('Nome: ')).strip())
    cadastro.append(float(input('Peso: ')))
    cont += 1
    pessoas.append(cadastro[:])
    cadastro.clear()
    for p in pessoas:
        if p[1] == 0:
            maior = menor = p[1]
        else:
            if p[1] > maior:
                maior = p[1]
            if p[1] < menor or menor == 0:
                menor = p[1]

    r = str(input('Quer continuar? [S/N] ')).strip()
    if r in 'Nn':
        break

print(f'Ao todo, você cadastrou {cont} pessoas')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p, v in enumerate(pessoas):
    if v[1] == maior:
        print(f'[{pessoas[p][0]}]',end=' ')

print()
print(f'O menor peso foi {menor}Kg. Peso de ', end='')
for p, v in enumerate(pessoas):
    if v[1] == menor:
        print(f'[{pessoas[p][0]}]',end=' ')






