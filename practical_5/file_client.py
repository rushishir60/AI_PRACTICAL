import socket

client = socket.socket()
client.connect(('localhost', 9999))

filename = 'sample.txt'  # File you want to send
with open(filename, 'rb') as f:
    data = f.read(1024)
    while data:
        client.send(data)
        data = f.read(1024)

print("File sent successfully!")
client.close()

