
soma = quant = media = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um número inteiro: '))
    quant += 1
    soma += n
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média entre todos os valores digitados é {:.0f}'.format(quant, media))
print('O maior valor é {} e o menor valor é {}'.format(maior, menor))
