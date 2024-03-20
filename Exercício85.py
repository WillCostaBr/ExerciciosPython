'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
 que mantenha separado os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. '''


lista = []

for c in range(1,8):
    num = int(input(f'Digite o {c}º valor: '))
    lista.append(num)

lista.sort()
print('-+'*30)
print(f'Os valores pares digitados foram ',end='')
for i,v in enumerate(lista):
    if v % 2 == 0:
        print(f'[{v}] ',end='')
print()
print(f'Os valores impares digitados foram ', end='')
for i, v in enumerate(lista):
    if v % 2 == 1:
        print(f'[{v}] ', end='')