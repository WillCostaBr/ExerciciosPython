'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação
e o salário. Calcule e acrescente, além d idade, com quantos anos a pessoa vai se aposentar'''

from datetime import date

pf = dict()

while True:
    pf["Nome"] = str(input('Nome: '))
    pf["Idade"] = int(input('Ano de Nascimento: '))
    pf["CTPS"] = int(input('Carteira de Trabalho (0 nao tem): '))
    if pf["CTPS"] == 0:
        break
    pf["Contratação"] = int(input('Ano de contratação: '))
    pf["Salário"] = float(input('Salário: R$ '))
    pf["Aposentadoria"] = 0

    pf["Aposentadoria"] = (pf["Contratação"] + 35) - pf["Idade"]
    break
pf["Idade"] = date.today().year - pf["Idade"]

print('-='*50)
print(pf)
for i,v in pf.items():
    print(f'{i} tem o valor {v}')

