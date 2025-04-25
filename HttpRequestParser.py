import socket

s = socket.socket()
s.bind(('localhost', 1234))
s.listen()

while True:
    conn, addr = s.accept()
    request_bytes = conn.recv(1024)
    request_str = request_bytes.decode()

    print("===== BYTES HTTP REQUEST =====")
    print(request_bytes)
    print("=============================")
    
    print()

    print("===== STR HTTP REQUEST =====")
    print(request_str)
    print("=============================")

    # Split the request into lines
    lines = request_str.split("\r\n")

    # First line is the request line
    request_line = lines[0]
    method, path, version = request_line.split(" ")
    print(f"TP Method: {method}")
    print(f"TP Path: {path}")
    print(f"TP HTTP Version: {version}")

    # Parsing headers
    headers = {}
    for line in lines[1:]:
        if line == "":
            break  # Empty line signifies end of headers
        header_name, header_value = line.split(": ", 1)
        headers[header_name] = header_value

    print("TP Headers:")
    for header, value in headers.items():
        print(f"{header}: {value}")

    conn.close()
