def leiadinheiro(msg):
    ok = False
    while True:
        p = str(input(msg)).strip().replace(',','.')
        if p.isalpha() or p == '':
            print(f'\033[0;31mERRO! "{p}" é um número inválido.\033[m')
        else:
            ok = True
            return float(p)