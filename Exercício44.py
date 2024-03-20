'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros
'''

from time import sleep

preco = float(input('Qual o valor do produto?\n'))
print('''Escolha a forma de pagamento:
[1] - à vista no dinheiro/cheque
[2] - à vista no cartão
[3] - 2x no cartão
[4] - 3x no cartão''')
pagamento = int(input(''))

sleep(1)
print('-+-'*10)
print('Processando...')
print('-+-'*10)
sleep(1)

d1 = (preco*10) / 100
avista = preco - d1
d2 = (preco*5) / 100
avistac = preco - d2
j = (preco*20) / 100
txc = preco + j

if pagamento == 1:
    print('Você ganhou 10% de desconto.\nO valor total do produto fica R${:.2f}'.format(avista))
elif pagamento == 2:
    print('Você ganhou 5% de desconto.\nO valor total do produto fica R${:.2f}'.format(avistac))
elif pagamento == 3:
    print('2x no cartão sem Juros.\n2 parcelas de R${:.2f}'.format(preco/2))
elif pagamento == 4:
    print('3x no cartão com juros de 20%.\nO valor total do produto fica R${:.2f}.\n3 parcelas de R${:.2f}'.format(txc,txc/3))
else:
    print('Opção Inválida.')