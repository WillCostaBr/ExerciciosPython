def metade(num = 0):
    tot = num / 2
    return tot

def dobro(num = 0):
    tot = num * 2
    return tot

def aumentar(num = 0, int = 0):
    tot = num + ((num * int) / 100)
    return tot

def diminuir(num = 0, int2 = 0):
    tot = num - ((num * int2) / 100)
    return tot

def moeda(num = 0, sigla = 'R$'):
    return f'{sigla}{num:.2f}'.replace('.',',')