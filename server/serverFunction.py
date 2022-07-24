from constants import *


def broadcast(clients: dict, clientSocket, message, len_msg):
    for key, value in clients.items():
        if key != clientSocket:
            key.send(len_msg.encode(FORMAT))
            key.send(message.encode(FORMAT))


def client_interaction(clientSocket, address, nickname):
    connection = True
    while connection:

        len_msg = clientSocket.recv(HEADER).decode(FORMAT)
        msg = clientSocket.recv(int(len_msg)).decode(FORMAT)

        print(f"[MESSAGE] {msg}. Sending to others clients...")

        if msg == DISCONNECT:
            clientSocket.close()
            print(f"[DISCONNECT] {nickname} disconnected. Sending to others clients...")
            msg = f"{nickname} disconnected."
            connection = False

        broadcast(clients, clientSocket, msg, str(len(msg)))