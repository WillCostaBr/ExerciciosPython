from random import randint
cont = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    soma = computador + jogador
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        if tipo == 'P':
            if tipo % 2 == 0:
                print('Você VENCEU!')
                cont += 1
            else:
                print('Você PERDEU!')
                break
        elif tipo == 'I':
            if tipo % 2 == 1:
                print('Você VENCEU!')
                cont += 1
            else:
                print('Você PERDEU!')
                break
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}')
