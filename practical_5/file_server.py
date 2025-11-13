import socket

server = socket.socket()
server.bind(('localhost', 9999))
server.listen(1)
print("Waiting for file...")

conn, addr = server.accept()
print("Connected with:", addr)

with open('received_file.txt', 'wb') as f:
    data = conn.recv(1024)
    while data:
        f.write(data)
        data = conn.recv(1024)

print("File received successfully!")
conn.close()
server.close()
