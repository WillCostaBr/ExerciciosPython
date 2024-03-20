#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Velocidade do carro: '))
multa = (vel - 80) * 7
if vel <= 80:
    print('\033[32mEstá dentro da velocidade limite.')
else:
    print('Ultrapassou a velocidade limite de 80Km.\nA multa será de \033[1:31mR${:.2f}\033[m'.format(multa))