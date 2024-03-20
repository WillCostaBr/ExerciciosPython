'''Aprimore o Exercício 86, mostrando no final:
a) a soma de todos os valores pares digitados
b) a soma dos valores da terceira coluna
c) o maior valor da segunda linha'''

matriz = [[0,0,0], [0,0,0], [0,0,0]]

soma = 0
mai = men = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[1][c] == 0:
            mai = men = matriz[1][c]
        else:
            if matriz[1][c] > mai:
                mai = matriz[1][c]
            if matriz[1][c] < men:
                men = matriz[1][c]
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma dos valores pares é {soma}.')


somat = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é {somat}.')
print(f'O maior valor da segunda linha é {mai}.')
