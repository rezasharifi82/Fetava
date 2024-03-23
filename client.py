import socket
import os
HOST = 'localhost'  # Replace with the actual server's hostname or IP address
PORT = 9090

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print('Connected to server')
ret=os.popen("hostname").read()
# message = input('Enter message to send to server: ')
message=("{}".format(ret))
client_socket.sendall(message.encode('utf-8'))

received_data = client_socket.recv(1024).decode('utf-8')
print(f'Received message from server: {received_data}')

client_socket.close()
