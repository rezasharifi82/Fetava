import socket
import os
import threading

def list_directory(path):
    try:
        return "\n".join(os.listdir())
    except FileNotFoundError:
        return "Directory not found."

def handle_client(control_socket, data_socket_port):
    while True:
        request = control_socket.recv(1024).decode("utf-8").strip()

        if request == "list":
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as data_socket:
                data_socket.bind(("127.0.0.1", data_socket_port))
                data_socket.listen(1)
                control_socket.sendall(str(data_socket_port).encode("utf-8"))

                data_client, data_client_address = data_socket.accept()
                directories = list_directory("./")
                data_client.sendall(directories.encode("utf-8"))
                data_client.close()

        elif request.lower().startswith("upload"):
            _, filename = request.split(" ", 1)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as data_socket:
                data_socket.bind(("127.0.0.1", data_socket_port))
                data_socket.listen(1)
                control_socket.sendall(str(data_socket_port).encode("utf-8"))

                data_client, data_client_address = data_socket.accept()

                content = data_client.recv(1024)
                with open(os.path.basename(filename), 'wb') as file:
                    file.write(content)

                data_client.close()

        elif request.lower().startswith("download"):
            _, filename = request.split(" ", 1)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as data_socket:
                data_socket.bind(("127.0.0.1", data_socket_port))
                data_socket.listen(1)
                control_socket.sendall(str(data_socket_port).encode("utf-8"))

                data_client, data_client_address = data_socket.accept()

                try:
                    with open(filename, 'rb') as file:
                        data = file.read()
                        data_client.sendall(data)
                except FileNotFoundError:
                    data_client.sendall("File not found".encode("utf-8"))

                data_client.close()
            
        elif request.lower().startswith("delete"):
            _, filename = request.split(" ", 1)
            try:
                os.remove(filename)
                control_socket.sendall("File deleted successfully".encode("utf-8"))
            except FileNotFoundError:
                control_socket.sendall("File not found".encode("utf-8"))
        elif request == "pwd":
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as data_socket:
                data_socket.bind(("127.0.0.1", data_socket_port))
                data_socket.listen(1)
                control_socket.sendall(str(data_socket_port).encode("utf-8"))

                data_client, data_client_address = data_socket.accept()
                data_client.sendall(os.getcwd().encode("utf-8"))
                data_client.close()
        
        elif request == "quit":
            break
        else:
            control_socket.sendall("Invalid command.".encode("utf-8"))

    control_socket.close()

def start_server(host, control_port, data_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, control_port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{control_port}")

    while True:
        control_client, control_address = server_socket.accept()
        print(f"Accepted connection from {control_address}")
        # handle_client(control_client, data_port)

        client_handler = threading.Thread(target=handle_client, args=(control_client, data_port))
        client_handler.start()

if __name__ == "__main__":
    CONTROL_PORT = 2121
    DATA_PORT = 2222
    start_server("127.0.0.1", CONTROL_PORT, DATA_PORT)