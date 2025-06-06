import socket

PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
BYTESIZE = 1024
DISCONNECT_MESSAGE = "quit"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

while True:
    message = client.recv(BYTESIZE).decode(FORMAT)

    if message == DISCONNECT_MESSAGE:
        client.send("quit".encode(FORMAT))
        print("You are about to disconnect from the server...")
        break
    else:
        print(f"{message}\n")
        message = input("Your Message: ")
        client.send(message.encode(FORMAT))

client.close()