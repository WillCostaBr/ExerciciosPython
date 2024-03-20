# Crie um programa que leia o nome de uma cidade e diga ou não se ela começa com a palavra 'SANTO'

cidade = str(input('Escreva o nome de uma cidade: ')).strip()
cidade = cidade.lower()
p = cidade.find('santo')

if p == 0:
    print('Essa cidade começa com a palavra santo')
else:
    print('Essa cidade não começa com a palavra santo')
