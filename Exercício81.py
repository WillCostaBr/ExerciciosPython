'''Crie um programa que vai ler varios números
e colocar em uma lista. Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores, ordenada de forma decrescente
c) Se o valor 5 foi digitado e está ou não na lista'''

lista = list()

cont = 0
r = 'Ss'

while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em forma decrescente são {lista}')
for i, v in enumerate(lista):
    if v == 5:
        print('O valor 5 faz parte da lista!')
        break
    else:
        print('O valor 5 não faz parte da lista!')
        break