# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome

nome = str(input('Digite o seu nome completo: '))
nome = nome.lower()
s = nome.find('silva')

if s <= 0:
    print('Seu nome não tem a palavra silva')
else:
    print('Seu nome tem a palavra silva')