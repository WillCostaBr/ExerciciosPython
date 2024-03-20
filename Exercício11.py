# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²

largura = int(input('Qual a largura da parede: '))
altura = int(input('Qual a altura da parede: '))

area = largura * altura
tinta = area / 2

print('Largura: {}\nAltura: {}\nTotal de tinta necessária: {:.0f} litros'.format(largura,altura,tinta))