'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso'''

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
     'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

'''while True:
     número = int(input('Digite um número entre 0 e 20: '))
     if número >= 0 and número <=20:
          break
     print('Tente novamente.', end='')
print(f'Você digitou o número {extenso[número]}')'''

pergunta = 'S'
número = 0
while pergunta not in 'N':
     número = int(input('Digite um número entre 0 e 20: '))

     if número >= 0 and número <= 20:
          print(f'Você digitou {extenso[número]}')
          pergunta = str(input('Quer continuar? [S/N]')).strip().upper()

     elif número <= 0 and número >= 20:
          print('Tente novamente.', end='')
          if pergunta == 'N':
               break

     else:
          break
print('PROGRAMA FINALIZADO.')





