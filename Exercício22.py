# Crie um programa que leia o nome completo de uma pessoa:
nome = str(input('Digite seu nome completo: ')).strip()


# O nome com todas as letras maiúsculas
print('Nome em letras maiúsculas: {}'.format(nome.upper()))

# O nome com todas as letras minúsculas
print('Nome em letras minúsculas: {}'.format(nome.lower()))

# Quantas letras têm (sem considerar espaços)
print('Quantidade total de letras: {}'.format(len(nome) - nome.count(' ')))

# Quantas letras tem o primeiro nome:
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))