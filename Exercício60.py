'''Faça um programa que leia um número qualquer e mostre o seu fatorial'''
'''ex: 5! 5 x 4 x 3 x 2 x 1 = 120'''

n1 = int(input('Digite um número: '))
cont = 1

for c in range(n1,0,-1):
    cont = cont * c
print(cont)