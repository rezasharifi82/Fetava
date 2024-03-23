import socket,pickle,os,useful,threading
class Transporter:
    def __init__(self,myip,destip) -> None:
        self.myip=myip
        self.destip=destip
        self.port=2121
        self.thred=threading.Thread(target=self.get)
        self.thred.start()
        # self.get()
        print("Transporter finilized!")


    def get(self):
        """
        Should be threaded
        This is a receiver method to check.
        no ls
        """
        port=self.port
        # import useful
        
        # ip=useful.get_my_ip()
        # ips=["192.168.1.107","192.168.1.108"]
        myip=self.myip
        # print
        destip=self.destip
        print("your ip is:"+str(myip))
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        add=(myip,port)
        print("wewe",add)
        s.bind(add)
        s.listen(5)
        print("here")
        while True:
            csock,cadd=s.accept()
            data=csock.recv(1024)
            obj=pickle.loads(data)
            print(obj)
            command=obj[0]
            something=obj[-1]
            print("someeeeeeeeeeeeeeee",something)
            sata=something
            if(int(obj[0])==0):
                #command
                sata=something
                if("pwd" in str(sata[0]).lower()):
                    d=os.popen("pwd")
                    d=list(d)[0][:-1]
                    print(d)
                    self.send(destip,(1,d))
                elif("get" in str(sata[0]).lower()):
                    path_to_file=sata[-1]
                    name_file=str(path_to_file).split("/")[-1]
                    size=0
                    seq_data=[]
                    with open(path_to_file,"rb") as f:
                        while True:
                            data=f.read(1024)
                            seq_data.append(data)
                            if not data:
                                break
                        self.send(destip,(2,name_file,seq_data),1)
                    
                # elif("send" in str(sata[0]).lower()):
                #     path_to_file=sata[-1]
                #     name_file=str(path_to_file).split("/")[-1]
                #     size=0
                #     seq_data=[]
                #     thing=(0,("get",path_to_file))
                #     self.send(self.destip,thing)

            elif(int(obj[0])==1):
                pass
            else:
                # obj=pickle.loads(something)
                # print("koi",data)
                name=data[1]
                data=obj[-1]
                
                with open("./"+str(name),"wb") as f:
                    f.write(data)
                    while True:
                        data=csock.recv(1024)
                        if (data is None):
                            break
                        # print("qqqq",data)
                        obj=pickle.loads(data)
                        data=obj[-1]
                        # print("qqkk",data)
                        if not data:
                            break
                        f.write(data)



    def file_sender(self,path):
        destip=self.destip
        print(777777777777777,destip)
        seq=[]
        ip=destip
        name=str(path).split("/")[-1]
        print(name)
        with open(path,"rb") as f:
            while True:
                data=f.read(1024)
                seq.append(data)
                if not data:
                    break
        # print(seq)
        packet=(2,name,seq)
        # packet=(ip,packet,1)
        self.send(ip,packet,1)
        return packet
                


        # packet=(2,(),1)
                
    def send(self,ip,thing,seq=0):
        port=self.port
        """
        This is a sender method that must be threaded\n
        ipadd: ip address of the destination\n
        **port:** port number of the destination\n
        **object:** this one is compound\n
        -----
        object=(command:boolean to see whether is it command or object,command or object)
        command = 0:command 1:python_object 
        
        
        
        fheader(file size):file(we should put file s ize in the header)
        
        sata:
        pwd: ("pwd",None)
        download : ("get" ,path)
        upload: ("send" , path)
        remove: ("rm", path)


        so for sending command:
        (0,("get",path))

        files:

        thing is 2D array (2,data)


        
        commnad is kind of string which can give me what to do

        thing is 2D tuple, (command,something)
        something if it is command -> we should pass an string
        """
        import pickle
        import socket
        flag=0
        print(4444)
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        while(flag==0):
            
            add=(ip,port)
            print(add)
            s.connect(add)
            flag=1
        if(seq==0):
            pickled=pickle.dumps(thing)
            s.sendall(pickled)
            s.close()
        else:
            print("UKK")
            first=thing[0]
            name=thing[1]
            sequence=thing[-1]
            for i in sequence:
                seting=((first,name,i))
                print("ioi",seting)
                pickled=pickle.dumps(seting)
                s.sendall(pickled)
            s.close()

# portal("192.168.1.107",(0,("pwd",0)))
# import os
# print(list(os.popen("pwd"))[0][:-1])
    

            

                
