'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
No final, mostre a mtriz na tela, com a formatação correta'''

#minha solução
'''linha1 = [[  ],[  ],[  ]]        
linha2 = [[  ],[  ],[  ]]
linha3 = [[  ],[  ],[  ]]

for c in range(0, 3):
    linha1[c].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0,3):
    linha2[c].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0,3):
    linha3[c].append(int(input(f'Digite um valor para [2, {c}]: ')))

print('-='*30)
print(linha1)
print(linha2)
print(linha3)'''

matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)


