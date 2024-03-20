# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$0,15 por Km rodado

km = int(input('Quantos Km você percorreu com o carro? '))
dia = int(input('Por quantos dias alugou o carro? '))

dias = dia * 60
kms = km * 0.15
ct = dias + kms

print('Total de dias: {}\nTotal de Km rodados: {}Km\nTotal a pagar: R${:.2f}'.format(dia,km,ct))