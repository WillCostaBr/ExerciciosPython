import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com.br')
except:
    print('O site não está acessível no momento')
else:
    print('Consegui acessar o site com sucesso')