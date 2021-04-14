from socket import *

serverPort = 14000 # porta onde o servidor estará rodando
#cria o Socket TCP (SOCK_STREAM) para rede IPv4(AF_INET)
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort)) # ligação do serviço a porta que foi estabelecida
#socket fica ouvindo conexões. O valor 1 indica que uma conexão pode ficar na fila
serverSocket.listen(1)

print('Servidor pronto para receber mensagens. Digite Ctrl + C para terminar')

while 1:
    #Cria um socket para tratar a conexão do cliente
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
