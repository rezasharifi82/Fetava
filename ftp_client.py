import socket
import os

def print_help():
    print("help - Display help information")
    print("list - List files on the server")
    print("upload <filename> - Upload a file to the server")
    print("download <filename> - Download a file from the server")
    print("delete <filename> - Delete a file on the server")
    print("pwd - Display current working directory on the server")
    print("quit - Quit the FTP client")

def connect():
    SERVER_HOST = "127.0.0.1"
    CONTROL_PORT = 2121

    control_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    control_socket.connect((SERVER_HOST, CONTROL_PORT))

    return control_socket

def main():
    control_socket = connect()

    while True:
        user_input = input("FTP> ").split()

        if not user_input:
            continue

        command = user_input[0].lower()

        if command == 'help':
            print_help()
        elif command == 'list':
            control_socket.sendall("list".encode("utf-8"))

            data_socket_port = int(control_socket.recv(1024).decode("utf-8"))

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as data_socket:
                data_socket.connect(("127.0.0.1", data_socket_port))
                data = data_socket.recv(1024).decode("utf-8")
                print(data)
        elif command == 'upload':
            if len(user_input) == 2:
                control_socket.sendall(f"upload {user_input[1]}".encode("utf-8"))

                data_socket_port = int(control_socket.recv(1024).decode("utf-8"))

                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as data_socket:
                    data_socket.connect(("127.0.0.1", data_socket_port))
                    
                    try:
                        with open(user_input[1], 'rb') as file:
                            data = file.read()
                            data_socket.sendall(data)
                    except FileNotFoundError:
                        print("File not found")
            else:
                print("Usage: upload <filename>")
        elif command == 'download':
            if len(user_input) == 2:
                control_socket.sendall(f"download {user_input[1]}".encode("utf-8"))

                data_socket_port = int(control_socket.recv(1024).decode("utf-8"))

                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as data_socket:
                    data_socket.connect(("127.0.0.1", data_socket_port))
                    data = data_socket.recv(1024).decode("utf-8")

                    if "File not found" in data:
                        print(data)
                    else:
                        with open(os.path.basename(user_input[1]), 'wb') as file:
                            file.write(data.encode("utf-8"))
                        print(f"File '{os.path.basename(user_input[1])}' downloaded successfully.")
            else:
                print("Usage: download <filename>")
        elif command == 'delete':
            if len(user_input) == 2:
                control_socket.sendall(f"delete {user_input[1]}".encode("utf-8"))
                log = control_socket.recv(1024).decode("utf-8")
                print(log)
            else:
                print("Usage: delete <filename>")
        elif command == 'pwd':
            control_socket.sendall("pwd".encode("utf-8"))

            data_socket_port = int(control_socket.recv(1024).decode("utf-8"))

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as data_socket:
                data_socket.connect(("127.0.0.1", data_socket_port))
                data = data_socket.recv(1024).decode("utf-8")
                print(data)
        elif command == 'quit':
            control_socket.close()
            print("Disconnected from FTP server.")
            break
        else:
            print("Invalid command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
