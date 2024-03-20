# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo

# Inclusive posso dizer qual tipo de triângulo pode ser formado.
# Não deve ser difícil isso em Python.

n1 = int(input('Indique o valor da primeira reta:\n'))
n2 = int(input('Indique o valor da segunda reta:\n'))
n3 = int(input('Indique o valor da terceira reta:\n'))

if n1 + n2 > n3 and n2 + n3 > n1 and n3 + n1 > n2:
    print('Essas retas formam um triângulo Escaleno')
elif n1 == n2 and n2 == n3 and n3 == n1:
    print('Essas retas formam um triângulo Equilátero')
elif n1 == n2 or n2 == n3 or n3 == n1:
    print('Essas retas formam um triângulo Isósceles')
else:
    print('Essas retas não formam nenhum tipo de triângulo')
