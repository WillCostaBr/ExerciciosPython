# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

real = float(input('Digite quantos reais você tem: '))

dolar = real * 5.35

print('R${:.2f} (real) = ${:.2f} (dólar)'.format(real,dolar))