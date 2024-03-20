#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
#e R$ 0,45 para viagens mais longas

dis = int(input('Digite a distância da viagem: '))

if dis <= 200:
    print('A viagem de {} custará R${:.2f}'.format(dis,dis*0.50))
else:
    print('A viagem de {} custará R${:.2f}'.format(dis,dis*0.45))