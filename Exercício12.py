# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Digite o vaor do produto:\n'))

valor = (produto * 5) / 100
total = produto - valor

print('Valor do produto com 5% de desconto é R${:.2f}'.format(total))