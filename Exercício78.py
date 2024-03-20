'''Faça um programa que leia 5 vlores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e menor valor digitado
e as sua respectivas posições na lista'''

valores = list()

maior = 0
menor = 0

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print('-'*30)
print(f'Você digitou os valores {valores}')
print('-'*30)

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i,v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i,v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')



'''for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''