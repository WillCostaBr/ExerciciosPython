# Desafio 18: Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians,sin,cos,tan
angulo = float(input('Digite o ângulo a ser calculado: '))

seno = sin(radians(angulo))
print('O ângulo de {}º tem o SENO {:.1f}'.format(angulo,seno))

cosseno = cos(radians(angulo))
print('O ângulo de {}º tem o COSSENO {:.1f}'.format(angulo,cosseno))

tangente = tan(radians(angulo))
print('O ângulo de {}º tem a TANGENTE {:.1f}'.format(angulo,tangente))