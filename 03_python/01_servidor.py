import socket
HOST, PORT = 127.0.0.1,2000

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(HOST,PORT)
tcp_server_socket.listen(1)
conn, addr = tcp_server_socket.accept()
print('Conexão de:'+addr)
while 1:
    data = conn.recv(1024)
    if not data: break
    print("\n Mensagem recebido:", data)
conn.close
