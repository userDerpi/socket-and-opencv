import socket
from textColored import Bcolors


class Server:
    PORT = 5000
    HEADER = 64
    FORMAT = "utf-8"
    DISCONNECT = "!LEAVE"

    def __init__(self):
        self._clients = {}
        self._IP = socket.gethostbyname(socket.gethostname())
        self._s = None

    @property
    def clients(self):
        return self._clients

    @clients.setter
    def clients(self, clients):
        self._clients = clients

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, s):
        self._s = s

    def initializeSocket(self):
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._s.bind((self.IP, self.PORT))
        self._s.listen()
        print(f"{Bcolors.OKGREEN} [RUNNING] Server is running...")

    def broadcast(self, clientSocket, message, len_msg):
        for key, value in self.clients.items():
            if key != clientSocket:
                key.send(len_msg.encode(self.FORMAT))
                key.send(message.encode(self.FORMAT))

    def handleClient(self, clientSocket, nickname):

        connection = True
        while connection:

            len_msg = clientSocket.recv(self.HEADER).decode(self.FORMAT)
            msg = clientSocket.recv(int(len_msg)).decode(self.FORMAT)

            print(f"{Bcolors.WARNING} [MESSAGE] {msg}. Sending to others clients...")
            msg = f"{Bcolors.OKCYAN} {msg}"

            if msg == self.DISCONNECT:
                clientSocket.close()
                print(f"{Bcolors.WARNING} [DISCONNECT] {nickname} disconnected. Sending to others clients...")
                msg = f"{Bcolors.WARNING} {nickname} disconnected."
                connection = False

            self.broadcast(clientSocket, msg, str(len(msg)))
