from time import sleep

lista = list()
notas = list()
continuar = 'S'
while continuar == 'S':
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    notas.append(nome)
    notas.append(nota1)
    notas.append(nota2)
    lista.append(notas[:])
    notas.clear()

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break


print('-='*20)

print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')

print('-'*30)

for i, aluno in enumerate(lista):
    media = (lista[i][1] + lista[i][2]) /2
    print(f'{i:<4}{lista[i][0]:<10}{media:>8}')
print('-'*30)

while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        break
    print(f'Notas de {lista[mostrar][0]} são {lista[mostrar][1]} e {lista[mostrar][2]}')
    print('-=' *20)

print('FINALIZANDO...')
sleep(2)
print('<<< VOLTE SEMPRE >>>')
