def metade(num=0, formato=False):
    tot = num / 2
    return tot if formato is False else moeda(tot)


def dobro(num=0, formato=False):
    tot = num * 2
    return tot if formato is False else moeda(tot)


def aumentar(num=0, taxa = 0, formato=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param num: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    tot = num + ((num * taxa) / 100)
    return tot if formato is False else moeda(tot)


def diminuir(num=0, taxa = 0, formato=False):
    tot = num - ((num * taxa) / 100)
    return tot if formato is False else moeda(tot)


def moeda(num=0, sigla = 'R$'):
    return f'{sigla}{num:.2f}'.replace('.',',')


def resumo(num=0, taxaa=0, taxab=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do Preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(num, taxaa, True)}')
    print(f'{taxab}% de redução: \t{diminuir(num, taxab,True)}')
    print('-'*30)