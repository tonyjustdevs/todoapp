import socket

client_socket = socket.socket()
# server_socket.bind("localhost")
client_socket.connect(("localhost", 12345))

client_socket.sendall(b'hello from client')
data_bytes = client_socket.recv(1024)

print(data_bytes)

client_socket.close()