'''Faça um programa que leia nome e média de um aluno, guardando tamém a situação em um dicionário.
No final mostre o conteúdo da estrutura na tela'''

aluno = {}
dados = list()

aluno["nome"] = str(input('Nome: '))
aluno["média"] = float(input(f'Média de {aluno["nome"]}: '))


print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["média"]}')
if aluno["média"] > 5:
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')
