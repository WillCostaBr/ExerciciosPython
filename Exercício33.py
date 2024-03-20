#Faça um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

maior = n1
if n3 > n2 and n3 > n1:
    maior = n3
elif n2 > n3 and n2 > n1:
    maior = n2
print('O maior valor é {}'.format(maior))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
print('O menor valor é {}'.format(menor))