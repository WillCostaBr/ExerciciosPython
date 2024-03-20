'''Crie um programa que tenh a função leiaint(), que vai funcionar de forma semelhante à função int do python,
só que fazendo a validação para aceitar apenas um valor numérico '''

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            ok = True
            valor = int(n)
        else:
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
