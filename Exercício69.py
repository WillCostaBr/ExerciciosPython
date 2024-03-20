''' Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostra:
a) quantas pessoas têm mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres têm menos de 20 anos'''

quantidade = 0
continuar = 'S'
homens = 0
mulheres = 0

while True:
    if continuar == 'S':
        print('-'*20)
        print('CADASTRE UMA PESSOA')
        print('-'*20)
        idade = int(input('Idade: '))
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
        continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
        if idade > 18:
            quantidade += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F':
            if idade < 20:
                mulheres += 1
    else:
        break
print(f'Total de pessoas com mais de 18 anos: {quantidade}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
print('Finalizando programa')
