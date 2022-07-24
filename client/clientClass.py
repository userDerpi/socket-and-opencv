import socket
from textColored import Bcolors


class Client:
    PORT = 5000
    HEADER = 64
    FORMAT = "utf-8"
    DISCONNECT = "!LEAVE"

    def __init__(self, nickname=""):
        self._nickname = nickname
        self._IP = socket.gethostbyname(socket.gethostname())  # TODO Change IP when comunication is not localhost
        self._s = None

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        self._nickname = nickname

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
        self._s.connect((self._IP, self.PORT))

    def sendMessage(self):

        def send_message(message: bytes):
            len_message = str(len(message)).encode(self.FORMAT)
            self._s.send(len_message)
            self._s.send(message)

        send_message(self._nickname.encode(self.FORMAT))  # to add the clients in server ledger

        connection = True
        while connection:
            message = f"{self._nickname}: {input('')}"
            print(f"{Bcolors.OKGREEN} {message}")
            send_message(message.encode(self.FORMAT))
            if message == self.DISCONNECT:
                connection = False
                print(f"{Bcolors.WARNING} Disconnection...")
                self._s.close()
                input('')

    def receiveMessage(self):
        while True:
            len_msg = self._s.recv(self.HEADER).decode(self.FORMAT)
            message = self._s.recv(int(len_msg)).decode(self.FORMAT)
            print(message)
