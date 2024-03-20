''' Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos
 '''

somaidade = 0
mediaidade = 0
maior = 0
menor = 0
nomehomemvelho = ''
mulherjovem = 0
for c in range(1,5):
    print('----{}ª pessoa----'.format(c))
    nome = str(input('Nome:\n'.format(c))).strip()
    idade = int(input('Idade:\n'))
    sexo = str(input('Sexo [M/F]:\n')).strip()
    somaidade = somaidade + idade

    if c == 1 and sexo in 'Mm':
        maior = idade
        nomehomemvelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomehomemvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulherjovem = mulherjovem + 1 #ou mulherjovem += 1
mediaidade = somaidade / 4
print('A media de idade do grupo é de {:.0f} anos'.format(mediaidade))
print('O nome do homem mais velho do grupo é {}'.format(nomehomemvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulherjovem))