'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''

valor = float(input("Qual o Valor da casa?\n"))
salario = float(input("Qual é o seu salário?\n"))
anos = int(input("Em quantos anos pretende pagar?\n"))

a = anos * 12
mensalidade = valor / a
porcento = (salario * 30) / 100

if mensalidade < porcento:
    print('Empréstimo Aprovado !!\nSua mensalidade será de R${:.2f}'.format(mensalidade))
else:
    print('Empréstimo negado!!\nO valor da mensalidade excede 30% por cento do seu salário!! ')