import socket
from datetime import datetime

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

name = input("Enter your name: ")

while True:
    msg = input()

    timestamp = datetime.now().strftime("%H:%M:%S")
    message = f"[{timestamp}] {name}: {msg}"

    client.send(message.encode())

    with open("chatlog.txt", "a") as f:
        f.write(message + "\n")
        