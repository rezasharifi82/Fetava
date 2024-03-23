class p:
    # import threading
    def __init__(self) -> None:
        self.ls_handler()
    def ls_handler(self):
        ip="192.168.1.108"
        import threading
        t1=threading.Thread(target=self.ls_listen)
        t1.start()
        t2=threading.Thread(target=self.ls_sender,args=[ip])
        t2.start()
        # self.ls_sender(ip)

    def ls_sender(self,ipadd):
        import pickle,socket,useful,time
        
        sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        add=(ipadd,2557)
        alls=[]
        print("Here @ ls sender",alls)
        # sock.connect(add)
        while(True):
            alls=useful.get_all_files(self.pwd())
            print("sender:  ",len(alls))
            data=pickle.dumps(alls)
            # print("In while")
            sock.sendto(data,add)
            time.sleep(5)
            # self.answer
        #
    def pwd(self):
        pwde="./"
        return pwde
    def ls_listen(self):
        import pickle,socket,useful,time,threading
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        ip=useful.get_my_ip()
        port=2557
        add=(ip,port)
        s.bind(("",port))
        # s.listen(5)
        # csock,cadd=s.accept()
        print(444)

        while True:
            print(11111)
            k=s.recvmsg(1024)
            print("In check",k)
            # threading.Thread(target=self.ls_sender,args=[cadd])
            data=k[0]
            data=pickle.loads(data)
            if(type(data) == list and len(data)>0):
                self.files=data.copy()
            time.sleep(2)

        # time.sleep(3)
            