import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen(5)

print("Server is running...")

client, addr = server.accept()
print(f"Connected: {addr}")

while True:
    message = client.recv(1024).decode()
    if not message:
        break
    print(message)

with open("chatlog.txt", "a") as f:
    f.write(message + "\n")

from datetime import datetime

time = datetime.now().strftime("%H:%M:%S")
message = f"[{time}] {name}: {msg}"