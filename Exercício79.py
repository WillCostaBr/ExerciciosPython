'''Crie um programa onde o usuário possa
digitar vários valores númericos e cadastre-os
em uma lista. Caso o número já exista lá
dentro, ele não será adicionado. No final,
serão exibidos todos os valores únicos digitados,
em ordem crescente.'''

lista = list()


while True:
    números = int(input('Digite um valor: '))
    if números not in lista:
        lista.append(números)
        print('Número adicionado com sucesso!')
    else:
        print('Número duplicado! Não vou adicionar.')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
lista.sort()
print(lista)