# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = str(input('Digite seu nome completo: ')).strip()

# Primeiro nome
f = nome.find(' ')
print('Seu primeiro nome é {}'.format(nome[0:f]))

# Último nome
rf = nome.rfind(' ')
print('Seu último nome é {}'.format(nome[rf:]))