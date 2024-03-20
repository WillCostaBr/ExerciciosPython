from ex115.lib.interface import *
from time import sleep
from ex115.lib.Arquivo import *

arq = '115.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resp = menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoa','Sair do Sistema'])
    if resp == 1:
        #opção de lista o conteúdo de um arquivo
        lerArquivo(arq)
    elif resp == 2:
        #opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do sistema... Até logo.')
        break
    else:
        print('ERRO! DIGITE UMA OPÇÃO VÁLIDA')
    sleep(3)