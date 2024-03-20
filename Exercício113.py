def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033\nO usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
             r = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31m\nO usuário preferiu não digitar esse número.\033[m')
            return 0
            break
        else:
            return r


n = leiaint('Digite um valor inteiro: ')
r = leiafloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n} e o real {r}.')