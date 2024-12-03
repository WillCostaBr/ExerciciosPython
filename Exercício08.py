# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = float(input('Digite o número a ser convertido: '))

dc = n * 10  #decímetros
cm = n * 100
mm = n * 1000
print('{:.0f} metros equivalem a {:.0F} decímetros {:.0f} centímetros {:.0f} milímetros'.format(n,dc,cm,mm))

dec = n / 10
hect = n / 100
km = n / 1000
print('{:.1f} decâmetros {:.1f} hectômetros e {:.1f} quilômetros'.format(dec,hect,km))