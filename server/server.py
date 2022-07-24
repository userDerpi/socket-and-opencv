import threading
from serverClass import Server

server = Server()
server.initializeSocket()

while True:
    clientSocket, address = server.s.accept()

    len_nick = clientSocket.recv(server.HEADER).decode(server.FORMAT)
    nickname = clientSocket.recv(int(len_nick)).decode(server.FORMAT)

    server.clients[clientSocket] = nickname

    thread = threading.Thread(target=server.handleClient, args=(clientSocket, nickname))
    thread.start()

    print(f"[CONNECTION] Connection established with {nickname}. Sending to others...")
    server.broadcast(clientSocket, f"{nickname} connected", str(len(f"{nickname} connected")))
