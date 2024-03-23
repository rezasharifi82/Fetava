import socket

HOST = 'localhost'  # Replace with the actual server's hostname or IP address
PORT = 9090

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print('Server is listening on port 9090')

while True:
    connection, client_address = server_socket.accept()
    print(f'Client connected from {client_address}')

    while True:
        data = connection.recv(1024).decode('utf-8')
        if not data:
            break

        print(f'Received message from client: {data}')

        # Send a response to the client
        response = 'Hello from the server!'
        connection.sendall(response.encode('utf-8'))

    connection.close()
