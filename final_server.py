import socket
import useful
import ftp_server
import logging
import threading
import re
class Server:
    shared=[]
    clients={}
    threads=[]
    def __init__(self) -> None:
        self.socket=useful.welcome_pack_server()
        self.broad=0
        self.ip=useful.get_my_ip()
        self.port=2273
        self.flag=True
        self.launch()
    
    def launch(self):
        self.flag=True
        t=threading.Thread(target=self.listening)
        Server.threads.append(t)
        t.setName("S:= Listening of Server Handshaking on port 2273")
        print("Launched!")
        t2=threading.Thread(target=self.broadcasting)
        t2.setName("S:= Broadcasting to clients on port 2273")
        Server.threads.append(t2)
        t.start()
        t2.start()
   
    def kill(self):
        self.broad.close()
        self.socket.close()
        self.flag=False
        

    def listening(self):# should be threaded
        while self.flag==True:
            k=self.socket.recvmsg(1024)
            adds=k[-1]
            port=int(adds[-1])
            ip=adds[0]
            d=str(k[0].decode())
            print("hello it's me")
            print(str(d))
            if(d.startswith("@Fetava") and self.hostname not in d):
                
                try:
                    # e=re.search("@Fetava,([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}),(.+)",d).groups()
                    e=d[8:]
                    e=e.split(",")
                    ip=e[1]
                    host=e[-1]
                    Server.clients[ip]=[host]
                    # print(e)
                    print("#New Client!!")
                    print(Server.clients.keys())
                    #e[1] is hostname
                except AttributeError:
                    print("#attr")
                except e:
                    print(logging.warning(e))   
        print("killed")
    def server_messsage(self):
        m=useful.get_message(True)
        self.os=m["OS"]
        self.hostname=m["hostname"]
        self.ip=m["IP"]
        m=m["message"]
        return m
        #Dont need ip and port
    def broadcasting(self):
        import socket
        import time

        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        server.settimeout(0.2)
        self.broad=server
        mm=self.server_messsage()
        message = mm.encode()
        while self.flag==True:
            server.sendto(message, ('<broadcast>', 2273))
            print("message sent! -> "+str(str(mm)))
            time.sleep(8)
