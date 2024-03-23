import socket
import threading
from tkinter import *
from PIL import Image
import GUI
import final_server
import final_client
# Server-side functions
def start_server():
    global server_socket

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("", 5000))
        server_socket.listen(5)
        print("Server started on port 5000")

        while True:
            connection, address = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(connection, address))
            thread.start()
    except Exception as e:
        print("Error starting server:", e)

def handle_client(connection, address):
    try:
        print("Client connected from", address)
        while True:
            data = connection.recv(1024).decode()
            if not data:
                break
            print("Client sent:", data)
            connection.sendall(data.upper().encode())
    finally:
        connection.close()
        print("Client disconnected")

# Client-side functions
def connect_to_server():
    global client_socket

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("127.0.0.1", 5000))
        print("Connected to server")

        while True:
            message = input("Enter message to send: ")
            if message == "quit":
                break
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024).decode()
            print("Server reply:", data)
    finally:
        client_socket.close()
        print("Disconnected from server")

def check():
    # canvas.destroy()
    print(234523)
g=GUI.gui()
print(324324)
print(g.buttons["Server"])
# g.buttons["Server"].pack()

