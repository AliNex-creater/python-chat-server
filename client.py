import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

name = input("Enter your name: ")

while True:
    message = input()
    client.send(f"{name}: {message}".encode())