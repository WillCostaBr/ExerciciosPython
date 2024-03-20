'''
Faça um programa que leia o sexo de uma pessoa
mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente
até ter um valor correto.
'''

sexo = str(input('Informe o sexo (\033[31mM\033[m - Masculino/\033[34mF\033[m - Feminino): ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados Inválidos: Por favor Informe o sexo: ')).strip().upper()
    '''if sexo == 'Masculino':
        print('O sexo informado foi Masculino. Registrado com sucesso!')
    elif sexo == 'Feminino':
        print('O sexo informado foi Feminino. Registrado com sucesso!')'''
print('O sexo informado foi \033[36m{}\033[m. Registrado com Sucesso!'.format(sexo))
