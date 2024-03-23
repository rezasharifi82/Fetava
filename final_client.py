import socket
import useful
import ftp_client
import logging
import threading
import re
class Client:
    shared=[]
    servers={}
    threads=[]
    def __init__(self) -> None:
        print("phase1")
        self.socket=useful.welcome_pack_client()

        self.ip=useful.get_my_ip()
        print("phase2"+str(self.ip))
        self.port=2273
        self.flag=True
        t=threading.Thread(target=self.launch)
        t.start()
        # self.launch()
    
    def launch(self):
        self.flag=True
        self.recv_broadcasting()
        self.get_up()
        self.kill()
   
    def kill(self):
        self.flag=False
        

    def get_up(self):# should be threaded
        server_ip=list(Client.servers.keys())[-1]
        details=Client.servers[server_ip]
        alpha=2
        while(alpha==2):
            try:
                self.socket.connect((server_ip,2273))
                alpha=1
            except:
                alpha=2
                import time
                time.sleep(2)
                print("I cant connect to server!! findout why!!!!!!!!!")
        message=self.client_messsage()
        print(message)
        m=message.encode()
        self.socket.send(m)
        print("Client acquired.")
        # print("killed")
    def client_messsage(self):
        m=useful.get_message(False)
        self.os=m["OS"]
        self.hostname=m["hostname"]
        self.ip=m["IP"]
        m=m["message"]
        return m

    def recv_broadcasting(self):
        import socket
        print("In recv")
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP
        client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        client.bind(("", 2273))
        while self.flag==True:
            data, addr = client.recvfrom(1024)
            ip=addr[0]
            port=addr[-1]
            host=""
            os=""
            print("Headsup!")
            print(data,addr)
            if(data.decode().startswith("@Fetava")):
                kk=data.decode()[8:]
                kk=kk.split(",")
                ip=kk[1]
                host=kk[-1]
                Client.servers[ip]=[host]

                print("received message: %s"%data)
                self.flag=False