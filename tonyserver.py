import socket

s=socket.socket()
s.bind(('localhost',12345))
s.listen()

while True:
    conn, addr = s.accept()
    request_bytes = conn.recv(1024)
    
    print("===== RAW REQUEST =====")
    print(request_bytes, type(request_bytes))
    
    request_decoded_str = request_bytes.decode()
    print(request_decoded_str, type(request_decoded_str))
    print("=======================")

    conn.sendall(b"g'day client!")
    conn.close()