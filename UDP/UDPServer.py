from socket import *

serverPort = 14000

#Cria o socket UDP (SOCK_DGRAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET, SOCK_DGRAM)

#Associa o Socket criado com a porta desejada
serverSocket.bind(('', serverPort))

print('Servidor pronto para receber mensagens. Digite Ctrl + C para terminar')

while 1:
    # Aguarda receber dados do socket
    message, clientAdress = serverSocket.recvfrom(2048)
    print(clientAdress)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAdress  )
