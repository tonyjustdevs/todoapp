# WSGI Application
# Is a function that accepts two arguments: 
# - arg_1: environ  (python dictionary)
#       - `environ` is how your server gives the request information to the WSGI app.
#       - It represents everything about the HTTP request: method, path, headers, etc.
#       - It's the input that the WSGI app reads to decide "what do I do?".
# - arg_2: start_response (a callable)
# - return: list of bytes? or iterable
def wsgi_application(environ, start_response):
    status_code = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status_code, response_headers)
    body = "G'day Mateys!"
    return [body.encode("utf-8")]

import socket
def wsgi_server(wsgi_application):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(1)

    with server_socket:
        client_socket, client_addr =  server_socket.accept()
        with client_socket:
            while True:
                data_bytes = client_socket.recv(1024)
                if not data_bytes:
                    break
                client_socket.sendall(b"g'day from server")
    
        
                result = wsgi_application()
                print(result)
        # result is an iterable or byte string: "G'day Mateys!"
        # 
if __name__ == "__main__":
    wsgi_server(wsgi_application)
