from socket import *

# canal virtual que é criado entre cliente e servidor 
serverName = '127.0.0.1' #quem é o servidor 
serverPort = 14000 # porta que o cliente irá utilizar para se comunicar
clientSocket = socket(AF_INET, SOCK_STREAM) # vinculo deste programa ao transporte (AF_INET -> Pilha ipv4) 
#                                            (SOCK_STREAM ->  socket utilizado para conexões TCP))
#                                            (SOCK_DGRAM -> socket utilizado para conexões UDP)

#conecta ao servidor
clientSocket.connect((serverName, serverPort))

# recebe mensagem do usuario e envia ao servidor
message = input('Digite uma frase: ')
clientSocket.send(message.encode('ascii'))

#aguarda mensagem de retorno e o imprime
modifiedMessage, addr = clientSocket.recvfrom(2048) #recebe no máximo 2018 bytes
print('Retorno do Servidor: ', modifiedMessage.decode())

clientSocket.close()