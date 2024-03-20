# Faça um programa que leia uma frase qualquer e mostre:
# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).lower().strip()

frase = frase.replace('á','a')
frase = frase.replace('à','a')
frase = frase.replace('ã','a')
frase = frase.replace('â','a')

# Quantas vezes aparece a letra "a"
print('Quantidade de letra A na frase: {}'.format(frase.count('a')))

# Em que posição ela aparece a primeira vez
print('Ela aparece a primeira vez na posição {}'.format(frase.find('a')+1))

# Em que posição ela aparece a última vez
print('Ela aparece a última vez na posição {}'.format(frase.rfind('a')+1))