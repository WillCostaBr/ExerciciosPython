'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de 1000 reais
C) Qual é o nome do produto mais barato'''

continuar = 'S'
total = 0
cont = 0
maisdemil = 0
maisbarato = 0
nomemaisbarato = 0

while True:
    if continuar == 'S':
        print('-'*20)
        print('LOJA SUPER BARATÃO')
        produto = str(input('Nome do produto: '))
        preço = int(input('Preço: '))
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        cont += 1
        total += preço
        if preço > 1000:
            maisdemil += 1
        if cont == 1:
            maisbarato = preço
            nomemaisbarato = produto
        else:
            if preço < maisbarato:
                maisbarato = preço
                nomemaisbarato = produto
    else:
        break
print(f'O total gasto é de R${total}')
print(f'Tem {maisdemil} produtos custando mais de R$1.000,00')
print(f'O produto mais barato é o {nomemaisbarato} e custa {maisbarato}')


