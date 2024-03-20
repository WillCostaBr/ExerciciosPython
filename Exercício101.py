'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições'''


def voto(calculo):
    from datetime import date
    ano = date.today().year
    global nascimento
    calculo = ano - nascimento
    if calculo <= 16:
        print(f'Com {calculo} anos: NÃO VOTA.')
    elif calculo > 16 and calculo < 65:
        print(f'Com {calculo} anos: VOTO OBRIGATÓRIO.')
    else:
        print(f'Com {calculo} anos: VOTO OPCIONAL.')
    return calculo


print('-='*40)
nascimento = int(input('Em que ano você nasceu? '))
voto(nascimento)

