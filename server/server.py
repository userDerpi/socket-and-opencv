import socket
import threading
import serverFunction
from constants import *

IP = socket.gethostbyname(socket.gethostname())

clients = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
print("[RUNNING] Server is running...")

s.listen()

while True:
    clientSocket, address = s.accept()

    len_nick = clientSocket.recv(HEADER).decode(FORMAT)
    nickname = clientSocket.recv(int(len_nick)).decode(FORMAT)

    clients[clientSocket] = nickname

    thread = threading.Thread(target=serverFunction.client_interaction, args=(clientSocket, address, nickname))
    thread.start()

    print(f"[CONNECTION] Connection established with {nickname}. Sending to others...")
    serverFunction.broadcast(clients, clientSocket, f"{nickname} connected", str(len(f"{nickname} connected")))
