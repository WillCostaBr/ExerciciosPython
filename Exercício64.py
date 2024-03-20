cont = 0
n = 0
soma = 0
n = int(input('Digite um número inteiro [999 para parar]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número inteiro [999 para parar]: '))
print('Foi digitado {} números, e a soma entre eles é {}'.format(cont, soma))