import socket,time
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("",4556))
while(True):
    print(5555)
    k=sock.recvmsg(1024)
    print(k)
    # time.sleep(1)