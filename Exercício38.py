'''Escreva um programa que leia dois números inteiro e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

n1 = float(input('Digite o Primeiro número '))
n2 = float(input('Digite o Segundo número: '))


if n1 > n2:
    print('O Primeiro valor é Maior')
elif n2 > n1:
    print('O Segundo valor é Maior')
else:
    print('Não existe valor maior, os dois valores são iguais')
