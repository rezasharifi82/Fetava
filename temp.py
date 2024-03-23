import socket,time
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while(1):
    sock.sendto("dasdasd".encode(),("192.168.111.222",4556))
    time.sleep(1)
    print("send")

