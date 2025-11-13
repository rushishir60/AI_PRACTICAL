import socket

# Create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 9999))  # server IP and port

print("UDP Server is ready to receive file...")

# Receive file name first
filename, addr = server.recvfrom(1024)
filename = filename.decode()
print("Receiving file:", filename)

with open('received_' + filename, 'wb') as f:
    while True:
        data, addr = server.recvfrom(4096)
        if not data:
            break
        if data == b'EOF':  # End of file
            break
        f.write(data)

print("File received successfully!")
server.close()
