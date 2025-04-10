import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# host = "127.0.0.1"
host = socket.gethostbyname(socket.gethostname())
port = 12345

serverSocket.bind((host, port))

serverSocket.listen()

while True:
    clientSocket, clientAdress = serverSocket.accept()

    print(f"Bağlantı yapıldı: {clientAdress}")
    print(clientSocket, clientAdress)

    clientSocket.send("Merhaba".encode("utf-8"))

    serverSocket.close()
    break