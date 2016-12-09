import socket
HOST = socket.gethostbyname('localhost')
PORT = 2000

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind((HOST,PORT))
tcp_server_socket.listen()
conn, addr = tcp_server_socket.accept()
print('Conexão de:', addr)
while True:
    data = conn.recv(1024)
    if not data: break
    print("\n Mensagem recebido:", data)
conn.close()
tcp_server_socket.close()
