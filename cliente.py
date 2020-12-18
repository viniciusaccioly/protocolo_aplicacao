from interface import *
from arquivos import * 
import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

client = []

def clientes(nome, cpf):
    client.append(nome)
    client.append(cpf)

def datas(ida,volta):
    client.append(ida)
    client.append(volta)

def lugar(assento):
    client.append(assento)


def enviar():
    msg= str(client)
    #msg= str(emitir())
    while True:
        tcp.send(str.encode(msg))
    tcp.close()


while True:
    resposta = menu(['Cadastro Cliente', 'Data ida e Volta','Assento(Lugar)', 'Emitir passagem', 'Sair'])
    if resposta == 1:
        name = input("Nome completo: ")
        cpf = int(input("numero cpf:"))
        clientes(name, cpf)
    elif resposta == 2:
        ida= input('Data de ida: ')
        volta = input("Data de volta: ")
        datas(ida, volta)
        #cabeçalho('Opção 2')
    elif resposta == 3:
        arquivo = input("Poltrona: ")
        lugar(arquivo)
        #cabeçalho('Opção 3')
    elif resposta == 4:
        #emitir()
        enviar()
    
    elif resposta == 5:
        cabeçalho('Operação Finalizada!')
        break    
    else:
        print('\033[31mERRO! Informe uma Opção Válida!\033[m')



