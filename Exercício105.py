'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
a) Quantidade de notas
b) A maior nota
c) A menor nota
d) A média de turma
e) A situação (opcional)'''

def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    print('_'*40)
    alunos = dict()
    soma = 0
    media = 0
    for c in num:
        soma += c
        media = soma / len(num)
    alunos['total'] = len(num)
    alunos['maior'] = max(num)
    alunos['menor'] = min(num)
    alunos['média'] = media
    if sit==True:
        if media >= 7:
            sit=True
            alunos['situação'] = str('BOA')
        if media > 5 and media < 7:
            sit=True
            alunos['situação'] = str('RAZOÁVEL')
        if media < 5:
            sit=True
            alunos['situação'] = str('RUIM')
    else:
        sit=False
    return alunos


#Programa Principal
resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
help(notas)
