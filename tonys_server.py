import socket

server = socket.socket()
server.bind(('localhost', 1234))
server.listen() # server is socket object

print("Listening on 127.0.0.1:1234...")

while True:
    conn, addr = server.accept()  
    # s.accept()  returns tuple 
    # conn: a new socket object - send and receive data to/from the client.)
    # addr: tuple containing the address (IP address and port number) of the client that connected.
    
    print(f"address of client ?: {addr}, {type(addr)}")
    
    
    request = conn.recv(1024)
    print("===== RAW REQUEST =====")
    print(request.decode()) 
    print("=======================")
    
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        "Content-Length: 13\r\n"
        "\r\n"
        "Hello, world!"
    )
    conn.send(response.encode())
    conn.close()