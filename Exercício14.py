# Conversor de temperaturas: escreva um programa que converta uma temperatura digitada em ºC para ºF

c = float(input('Digite os graus celsius:\n'))
f = (c * 1.8) + 32

print('{:.0f}ºC equivalem a {}ºF.'.format(c,f))
