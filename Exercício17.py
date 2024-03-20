# Desafio 17: Faça um programa que leia o comprimento do cateto oposto (co) e do cateto adjacente (ca) de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

import math

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

hipo = (co **2) + (ca**2)
print('A hipotenusa do triângulo retângulo é {:.1f}'.format(hipo))