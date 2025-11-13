import socket

server_address = ('localhost', 9999)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Enter filename to send: ")  # e.g., sample.txt, script.py, song.mp3, video.mp4

# Send the filename first
client.sendto(filename.encode(), server_address)

# Send file in chunks
with open(filename, 'rb') as f:
    data = f.read(4096)
    while data:
        client.sendto(data, server_address)
        data = f.read(4096)

# Send EOF to indicate file end
client.sendto(b'EOF', server_address)

print("File sent successfully!")
client.close()
