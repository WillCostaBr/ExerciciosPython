a = input('Digite algo: ')
print('O tipo primitivo desse valor é ',type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('è alfabético?', a.isalpha())
print('É alfanumérico?',a.isalnum())
print('Está em maiúsculas?', a.islower())
print('Está em minúsculas?', a.isupper())
print('Está capitalizada?', a.istitle())