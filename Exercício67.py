'''Faça um programa que leia a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário
O programa será interrompido quando o númeor solicitado for negativo'''

while True:
    print('-'*20)
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*20)
    if tabuada < 0:
        break
    for c in range(1,11):
        print('{} x {} = {}'.format(tabuada, c, tabuada*c))
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')