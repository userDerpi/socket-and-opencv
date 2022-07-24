import socket
import threading
from textColored import Bcolors
from clientClass import Client

user = Client()
user.nickname = input("Type your nickname: ")

try:

    user.initializeSocket()
    send_thread = threading.Thread(target=user.sendMessage)
    send_thread.start()

    receive_thread = threading.Thread(target=user.receiveMessage)
    receive_thread.start()

except socket.error or threading.ThreadError:
    print(f"{Bcolors.FAIL} An erros has occured")
