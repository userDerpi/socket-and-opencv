import socket

PORT = 5000
IP = socket.gethostbyname(socket.gethostname())
HEADER = 64
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
print("[RUNNING] Server is running...")

s.listen()

while True:
    clientSocket, address = s.accept()
    print(f"[CONNECTION] Connection established from {address}")

    len_msg = clientSocket.recv(HEADER).decode(FORMAT)
    msg = clientSocket.recv(int(len_msg)).decode(FORMAT)

    print(f"[MESSAGE] Client {address} writes: {msg}")
    clientSocket.send(bytes("Welcome to the server!!!","utf-8"))
    clientSocket.close()