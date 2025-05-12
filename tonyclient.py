import socket

import selectors
print(type(selectors.DefaultSelector()))

client_socket = socket.socket()
client_socket.connect(('localhost',12345))

# conn, addr = s.accept()
client_socket.sendall(b"g'day server from tonyclient.py!")

server_response_bytes = client_socket.recv(1024)

print("===== RAW RESPONSE =====")
print(server_response_bytes, type(server_response_bytes))

server_response_str = server_response_bytes.decode()
print(server_response_str, type(server_response_str))
print("=======================")

client_socket.close()