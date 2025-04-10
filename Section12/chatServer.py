import socket

PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
BYTESIZE = 1024
DISCONNECT_MESSAGE = "quit"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

server.listen()
print("Server is working...\n")

clientSocket, clientAdress = server.accept()
clientSocket.send("You are now connected to the server.\n".encode(FORMAT))

while True:
    message = clientSocket.recv(BYTESIZE).decode(FORMAT)

    if message == DISCONNECT_MESSAGE:
        clientSocket.send("quit".encode(FORMAT))
        print("You have disconnected from the server.")
        break
    else:
        print(f"{message}\n")
        message = input("Your Message: ")
        clientSocket.send(message.encode(FORMAT))

server.close()