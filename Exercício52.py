n = int(input('Digite um valor: '))

#if n % n == 0:
    #print('{} é um número primo'.format(n))

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
    else:
        print('\033[m', end='')
print('{} '.format(c), end='')

'''for num in [12,34,2,45,54]:
    print(num)
print('fim do programa')'''