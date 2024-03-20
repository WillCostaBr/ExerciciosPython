# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

nome = input('Digite o nome do funcionário:\n')
salario = float(input('Digite o salário:\n'))

calculo = (salario * 15) / 100
aumento = salario + calculo

print('Nome: {}\nSalário atual: R${:.2f}\nSalário com 15% de aumento: R${:.2f}'.format(nome,salario,aumento))