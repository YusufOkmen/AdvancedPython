import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 12345

clientSocket.connect((host, port))

message = clientSocket.recv(1024)

print(message.decode("utf-8"))

clientSocket.close()