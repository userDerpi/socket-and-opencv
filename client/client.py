import socket
import threading
import clientFunction
from constants import *

IP = socket.gethostbyname(socket.gethostname())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

nickname = input("Type your nickname: ")

send_thread = threading.Thread(target=clientFunction.send, args=(s, nickname))
send_thread.start()

receive_thread = threading.Thread(target=clientFunction.receive)
receive_thread.start()
