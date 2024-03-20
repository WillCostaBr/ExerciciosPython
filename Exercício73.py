'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados
b) Os últimos 4 colocados da tabela
c) Uma lista com os times em ordem alfabética
d) Em que posição na tabela está o time da chapecoense'''

times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Bragantino', 'Fluminense', 'Atlhético - PR', 'Flamengo', 'Fortaleza',
         'Atlético - MG', 'Chapecoense', 'Corinthians', 'Cuiabá', 'Cruzeiro', 'Internacional', 'Vasco da Gama', 'Goiás',
         'Bahia', 'Santos', 'América-MG', 'Coritiba')
print('-='*20)
print(f'Lista de times do Brasileirão: {times}')
print('-='*20)
print(f' Os 5 primeiros colocados são: {times[0:5]}')
print('-='*20)
print(f' Os Últimos 4 colocados são: {times[16:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*20)
if 'Chapecoense' in times:
    print('O Chapecoense está na 'f'{times.index("Chapecoense")+1}ª posição')
else:
    print('Chapecoense não se encontra na lista')
