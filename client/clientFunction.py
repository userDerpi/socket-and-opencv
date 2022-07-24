from constants import *
import socket


def send_message(s: socket, message: bytes):
    len_message = str(len(message)).encode(FORMAT)
    s.send(len_message)
    s.send(message)


def send(s: socket, nickname):
    try:
        send_message(s, nickname.encode(FORMAT))

        connection = True
        while connection:
            message = f"{nickname}: {input('')}".encode(FORMAT)
            send_message(s, message)
            if message.decode(FORMAT) == DISCONNECT:
                connection = False
                s.close()

    except socket.error:
        print("An errors is occured")


def receive(s: socket):
    while True:
        len_msg = s.recv(HEADER).decode(FORMAT)
        message = s.recv(int(len_msg)).decode(FORMAT)
        print(message)
