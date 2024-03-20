def metade(num = 0, formato=False):
    tot = num / 2
    return tot if formato is False else moeda(tot)

def dobro(num = 0, formato=False):
    tot = num * 2
    return tot if formato is False else moeda(tot)

def aumentar(num = 0, int = 0, formato=False):
    tot = num + ((num * int) / 100)
    return tot if formato is False else moeda(tot)

def diminuir(num = 0, int2 = 0, formato=False):
    tot = num - ((num * int2) / 100)
    return tot if formato is False else moeda(tot)

def moeda(num = 0, sigla = 'R$'):
    return f'{sigla}{num:.2f}'.replace('.',',')