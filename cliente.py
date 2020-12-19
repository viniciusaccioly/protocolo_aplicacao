from interface import *
import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

client = []

def clientes(nome, cpf):
    nNome="NOME:"+ nome
    nCpf= "CPF:" + cpf
    client.append(nNome)
    client.append(nCpf)

def datas(ida,volta):
    nIda = "Ida:" +ida
    nVolta = "Volta:" + volta
    client.append(nIda)
    client.append(nVolta)

def lugar(assento):
    asse= "Assento:" + assento
    client.append(asse)


def enviar():
    msg= str(client)
    while True:
        tcp.send(str.encode(msg))
        break
        
def emitir():
    print("\n", client[0], "\n", client[1], "\n", client[2], "\n", client[3], "\n", client[4])
    print("\nBoa viagem!")

while True:
    resposta = menu(['Cadastro Cliente', 'Data ida e Volta','Assento(Lugar)', 'Emitir passagem', 'Sair'])
    if resposta == 1:
        name = input("Nome completo: ")
        cpf = input("Numero cpf:")
        clientes(name, cpf)
    elif resposta == 2:
        ida= input('Data de ida: ')
        volta = input("Data de volta: ")
        datas(ida, volta)
    elif resposta == 3:
        arquivo = input("Poltrona: ")
        lugar(arquivo)
    elif resposta == 4:
        enviar()
        emitir()
    elif resposta == 5:
        cabeçalho('Operação Finalizada!')
        tcp.close()
        break    
    else:
        print('\033[31mERRO! Informe uma Opção Válida!\033[m')



