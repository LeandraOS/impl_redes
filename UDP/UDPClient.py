from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# no UDP, a forma de conexão entre cliente e servidor é sutil e não requer a conexão direta.

# recebe mensagem do usuário e envia ao destino
message = input('Digite uma frase: ')
clientSocket.sendto(message.encode('ascii'),(serverName, serverPort)) # por não haver conexão direta, 
#é sempre necessário receber a cada nova comunicação o servidor e a porta.

#aguarda mensagem de retorno e a imprime
modifiedMessage, serverAdress = clientSocket.recvfrom(2048)
print('Retorno do Servidor: ' + modifiedMessage.decode())

clientSocket.close()
 