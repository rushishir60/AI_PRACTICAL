import socket

# Create TCP socket
server = socket.socket()
server.bind(('localhost', 9999))   # host = localhost, port = 9999
server.listen(1)

print("Server is waiting for connection...")

conn, addr = server.accept()
print("Connected with:", addr)

# receive message from client
msg = conn.recv(1024).decode()
print("Client says:", msg)

# send reply to client
conn.send("Hello Client, how are you?".encode())

conn.close()
server.close()
