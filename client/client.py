import socket

PORT = 5000
IP = socket.gethostbyname(socket.gethostname())
FORMAT = "utf-8"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    message = input("Type a message to send to the server: ").encode(FORMAT)
    len_msg = str(len(message)).encode(FORMAT)

    s.send(len_msg)
    s.send(message)
except socket.error:
    print(f"Error in connection to the server")
