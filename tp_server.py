import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("localhost", 12345))
server_socket.listen(5)

with server_socket:
    client_socket, client_addr =  server_socket.accept()
    with client_socket:
        while True:
            data_bytes = client_socket.recv(1024)
            if not data_bytes:
                break
            data = data_bytes.decode()
            
            data_list = data.splitlines()
            print(data_list, type(data_list))
            http_header_list =  data_list[0].split()
            http_method = http_header_list[0]
            http_path = http_header_list[1]
            http_version = http_header_list[2]
            
            print(f"tonys_http_method: {http_method}")
            print(f"tonys_http_path: {http_path}")
            print(f"tonys_http_version: {http_version}")
            
            other_http_headers_list = data_list[1:]
            tonys_headers = {}
            for header in other_http_headers_list[:-1]:
                # header_key, header_val = header.split(": ")
                header_key_val_list = header.split(": ")
                http_header_key = header_key_val_list[0]
                http_header_val = header_key_val_list[1]
                tonys_headers[http_header_key] = http_header_val
                print(f"tonys_headers: {tonys_headers}")
            client_socket.sendall(b'Hello from server')
            
            
            



environ["REQUEST_METHOD"]="GET" # "GET" OR "POST"
environ["SCRIPT_NAME"]=""       # empty string okay
environ["PATH_INFO"]="/"        # or "/hello" or empty string okay
environ["QUERY_STRING"]=""      # empty string or absent okay
environ["CONTENT_TYPE"]=""      # empty string or absent okay
environ["CONTENT_LENGTH"]=""    # empty string or absent okay
environ["SERVER_NAME"]          ="localhost"
environ["SERVER_PORT"]          = "12345"
environ["SERVER_PROTOCOL"]      ="HTTP/1.0"   # "HTTP/1.0" or "HTTP/1.1"
environ["HTTP_Variables"]=""

import sys            
wsgi.version        = (1,0)
wsgi.url_scheme     = "http"    # or https
wsgi.input          = " ??? "
wsgi.errors         = sys.stderr
wsgi.multithread    = False
wsgi.multiprocess   = False
wsgi.run_once       = False