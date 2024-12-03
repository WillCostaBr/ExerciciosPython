# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:

num = float(input('Digite um número qualquer: '))

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print('O número é {}\nSeu dobro é {}\nSeu triplo é {}\nE sua raiz é {}'.format(num,dobro,triplo,raiz))