import socket
serverHost = socket.gethostbyname('10.25.1.233')
serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind((serverHost, serverPort))

print('O servidor está pronto para receber:')
#print('Conexão de:', addr)

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('Conexão de:', clientAddress)
    #processa a string para letras maiúsculas
    modifiedMessage = message.upper()
    print("\n", modifiedMessage)
    serverSocket.sendto(modifiedMessage, clientAddress)
