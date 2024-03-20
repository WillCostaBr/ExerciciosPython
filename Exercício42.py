'''
Refaça o DESAFIO 35, dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:
- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes
'''

a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if (a + b) > c and (b + c) > a and (c + a) > b:
    print('É possível formar um triângulo com essas retas')
    if a == b and b == c and c == a:
        print('Triângulo Equilátero')
    elif (a == b) or (b == c) or (c == a):
        print('Triângulo Isósceles')
    elif a != b and b != c and c != a:
        print('Triângulo Escaleno')
else:
    print('Não é possível formar um triângulo')

