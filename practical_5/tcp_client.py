import socket

client = socket.socket()
client.connect(('localhost', 9999))

# send message to server
client.send("Hello Server!".encode())

# receive reply from server
msg = client.recv(1024).decode()
print("Server says:", msg)

client.close()
