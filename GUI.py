import socket
import threading
# import temp
from tkinter import *
from tkinter import filedialog
from PIL import Image
import final_server
import final_client
import pickle,useful,air
class gui:
    canvas={}
    root=0
    flag=True
    buttons={}
    temp=[]
    files=[]

    def __init__(self):
        
            # Create the main window
        root = Tk()
        root.title("Fetava")
        root.focus()
        gui.root=root
        image=PhotoImage(file = "nasa.png") 
        # photo = ImageTk.PhotoImage(image)
        gui.canvas["main"]=Canvas(root,width=400,height=400)
        canvas=gui.canvas["main"]
        canvas.pack(fill="both",expand=True)
        canvas.create_image(-300,-300,image=image,anchor="nw")
        # root.configure(bg=image)
        # root.configure(i)
        # Server button
        self.myip=useful.get_my_ip()
        self.destip=0
        self.myhost=useful.generate_info()["Name"]
        self.desthost="Archlinux"
        #-------------------------------------------------------------------------
        server_button = Button(canvas, text="Server")
        
        client_button = Button(canvas, text="Client")
        #-------------------------------------------------------------------------
        gui.buttons["Server"]=server_button
        gui.buttons["Client"]=client_button
        # gui.canvas=canvas
        ##################################################3333
        server_button.configure(command=self.inii_server_page)
        # server_button.configure(command=self.ftp_server_page)
        client_button.configure(command=self.inii_client_page)
        server_button.configure(background='#%02x%02x%02x' % (173, 252, 3),activebackground='#%02x%02x%02x' % (227, 177, 138),font=("TimesNewRoman",19,"italic"))
        # server_button.
        server_button.place(width=100,height=80,x=20,y=20)
        
        # Client button
        
        client_button.configure(background='#%02x%02x%02x' % (209, 169, 214),activebackground='#%02x%02x%02x' % (169, 214, 196),font=("TimesNewRoman",19,"italic"))
        label=Label(canvas,text="Fetava",bg='#%02x%02x%02x' % (173, 252, 3),font=("Arial",25,"italic"))

        client_button.place(width=100,height=80,x=280,y=290)
        label.place(width=130,height=80,x=130,y=150)
        canvas.configure(height=400,width=400)
        
        # Start the main loop
        root.mainloop()

    def threaded_listbox(self,listbox,ip_dict:dict):
        while gui.flag==True:
            listbox.delete(0,END)
            # print(self.temp)
            k=0
            for i,j in ip_dict.items():
                m=str(k+1)+" - "+str(i)+"  , "+str(j[0])
                listbox.insert(END,m)
                # print(listbox.END)
                k+=1
            listbox.place(x=60,y=100)
            # print(listbox.curselection())
            import time
            time.sleep(5)
    def inii_client_page(self):
        # import temp
        import pickle
        self.client=final_client.Client()
        self.client_ip_list=self.client.servers
        gui.canvas["main"].pack_forget()
        temp=Canvas(gui.root,width=400,height=400)
        
        label=Label(temp,text="Server Initialized",font=("TimesNewRoman",30,"bold"),bg="#d6c187",fg="#360809")
        temp.config(bg="#d6c187")
        label.place(width=320,height=40,x=40,y=15)
        Label(temp,text="Wait for discovery...",font=("TimesNewRoman",20,"italic"),bg="#d6c187",fg="#360809").place(width=320,height=20,x=40,y=100)
        # listbox=Listbox(temp,width=25,height=8,background="#91dbbf",font=("Arial",15,"italic"),xscrollcommand=True,yscrollcommand=True)
        # gui.flag==True
        # t=threading.Thread(target=self.threaded_listbox,args=[listbox,self.client_ip_list])
        # t.start()
        temp.pack()
        
        # t1=threading.Thread(target=listbox.curselection)
        # t1.start()
        # text=Entry(temp,font=("Arial",16,"italic"))
        # text.place(x=170,y=320,height=30,width=50)
        current=0
        answer=0
        # text.bind("<Return>", lambda event: print(answer:= self.returner(self.client_ip_list,text)))
        
        # print(listbox.curselection())

        # print("FOrget###########")
        # temp.pack_forget()
        gui.canvas["client"]=temp
        t=self.listen_client_page()
        print("hereeeeeeee")
        
        # button = Button(temp, text="Back", command=lambda: self.switcher("main"))
        # button.place(x=135,y=360)      
        
    def inii_server_page(self):
        # import temp
        self.server=final_server.Server()
        self.server_ip_list=self.server.clients
        gui.canvas["main"].pack_forget()
        temp=Canvas(gui.root,width=400,height=400)
        
        label=Label(temp,text="Server Initialized",font=("TimesNewRoman",30,"bold"),bg="#d6c187",fg="#360809")
        temp.config(bg="#d6c187")
        label.place(width=320,height=40,x=40,y=15)
        Label(temp,text="(Just Enter the number of your option)",font=("TimesNewRoman",10,"italic"),bg="#d6c187",fg="#360809").place(width=320,height=20,x=40,y=60)
        # scrollbar = Scrollbar(temp, orient='horizontal', command=listbox.xview)
        # scrollbar.place(x=130,y=130)
        # scrollbar_y = Scrollbar(temp, orient='vertical', command=listbox.yview)
        # scrollbar_y.pack(side=RIGHT, fill=BOTH)
        
        listbox=Listbox(temp,width=25,height=8,background="#91dbbf",font=("Arial",15,"italic"),xscrollcommand=True,yscrollcommand=True)
        gui.flag==True
        t=threading.Thread(target=self.threaded_listbox,args=[listbox,self.server_ip_list])
        t.start()
        
        
        t1=threading.Thread(target=listbox.curselection)
        t1.start()
        text=Entry(temp,font=("Arial",16,"italic"))
        text.place(x=170,y=320,height=30,width=50)
        current=0
        answer=0
        text.bind("<Return>", lambda event: print("Submit!"))
        
        # print(listbox.curselection())

        # self.answer=answer
        # self.answer=text.get()
        button = Button(temp, text="Connect", command= lambda : self.returner(self.server_ip_list,text))
        button.place(x=135,y=360)      
        gui.canvas["server"]=temp
        temp.pack()
    def transporter(self):
        self.transp=air.Transporter(self.myip,self.destip)
        # self.transporter.send()
        # self.transp
        # self.transporter.

    def ls_handler(self):
        ip=self.dest
        t1=threading.Thread(target=self.ls_listen)
        t1.start()
        t2=threading.Thread(target=self.ls_sender,args=[ip])
        t2.start()

    def ls_sender(self,ipadd):
        import pickle,socket,useful,time
        alls=useful.get_all_files(self.pwd())
        sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        add=(ipadd,2557)
        # print("Here @ ls sender",add)
        # sock.connect(add)
        while(True):
            alls=useful.get_all_files(self.pwd())
            print("You see"+str(len(alls)))
            data=pickle.dumps(alls)
            # print("In while",data)
            sock.sendto(data,add)
            print("Packet send",add)
            time.sleep(5)
            # self.answer
        #
    def pwd(self,path=""):
        pwde="./"+path
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
        print("In Listen")
        while True:
            k=s.recvmsg(1024)
            # print("In check",k)
            # threading.Thread(target=self.ls_sender,args=[cadd])
            data=k[0]
            # print("I mean",k)
            data=pickle.loads(data)
            if(type(data) == list and len(data)>0):
                # self.files=data.copy()
                self.files=data
                print("I seeeeeeee"+str(len(data)))
                print("FFF seeeeeeee"+str(len(self.files)))
            time.sleep(2)
            
    def other_ls(self,canvas):  
        import useful,time
        
        print(111111111,len(self.files))
        from tkinter import ttk
        while(True):
            files=self.files
            print("youkniw")
            tv=ttk.Treeview(canvas)
            tv["columns"]=["ID","Type","Path","Size","Name"]
            tv.column("#0",width=0,minwidth=0)
            tv.column("ID",width=30,minwidth=30)
            tv.column("Type",width=50,minwidth=30)
            tv.column("Path",width=100,minwidth=50)
            tv.column("Size",width=100,minwidth=30)
            tv.column("Name",width=100,minwidth=50)

            tv.heading("ID",text="ID",anchor='w')
            tv.heading("Type",text="Type",anchor='w')
            tv.heading("Path",text="Path",anchor='w')
            tv.heading("Size",text="Size",anchor='w')
            tv.heading("Name",text="Name",anchor='w')
            # tv.delete()
            for i,row in enumerate(files):
                opo=[i+1]
                opo.extend(row)
                tv.insert("",i,values=opo)

            tv.place(x=60,y=90)
            time.sleep(5)
            print("ohio")
            tv.destroy()

    def ls_otherside(self,canvas):
        import useful,time
        print("log")
        self.ls_handler()
        threading.Thread(target=self.other_ls,args=[canvas]).start()

    
    def ftp_server_page(self):
        self.transporter()
        gui.canvas["server"].pack_forget()
        temp=Canvas(gui.root,width=500,height=500)
        label=Label(temp,text="Server File Options",font=("TimesNewRoman",30,"bold"),bg="#74e391",fg="#360809")
        temp.config(bg="#74e391")
        label.place(width=360,height=40,x=70,y=25)
        # print(555555550)
        self.dest=self.answer[0]
        tobe="Dest : "+str(self.answer[0])+"   "+str(self.answer[-1])
        Label(temp,text=tobe).place(x=0,y=0)
        # Label(temp,text="(Just Enter the number of your option)",font=("TimesNewRoman",10,"italic"),bg="#d6c187",fg="#360809").place(width=320,height=20,x=40,y=60)
        
        # listbox=Listbox(temp,width=25,height=8,background="#91dbbf",font=("Arial",15,"italic"),xscrollcommand=True,yscrollcommand=True)
        self.ls_otherside(temp)





#############################################################
        text=Entry(temp,font=("Arial",16,"italic"))
        text.place(x=170,y=320,height=30,width=50)
        current=0
        answer=0
        text.bind("<Return>", lambda event: print("Submit!"))
        
        try:
            answer=int(text.get())
        except:
            print("Not Valid Entry!")
        
        nows=self.files.copy()
        download=Button(temp,text="Download",command=lambda : self.download(answer,nows))
        # download.grid_location(x=50,y=50)
        download.place(x=60,y=450)
        pata=""
        upload=Button(temp,text="Upload",command=lambda : (pata:=self.upload()))
        print(pata)
        # download.grid_location(x=50,y=50)
        upload.place(x=150,y=450)

        remove=Button(temp,text="Remove",command=lambda : (pata:=self.delete(answer,nows)))
        print(pata)
        # download.grid_location(x=50,y=50)
        remove.place(x=300,y=450)




        gui.canvas["ftpser"]=temp
        temp.pack()
    def choose_file(self):
        filename = filedialog.askopenfilename(
            title="Fetava File selector",
            filetypes=(("All files", "*.*"), ("Text files", "*.txt"))
        )
        if filename:
            # Do something with the selected file path, e.g., display it or process it
            print(f"Selected file: {filename}")
        return filename

    def download(self,index,files):
        index-=1
        current=files[index]
        path=str(current[-3])
        print("jjjjjjjj",path)
        # ID  Type  Path  Size  Name
        try:
            useful.set_file(path)
            self.transp.send(self.destip,(0,"get "+path))
        except:
            pass
        # self.transp.get()


    def upload(self):
        pata=self.choose_file()
        path=pata
        try:
            useful.handshake(source=path)
            print("omega",path)
            self.transp.file_sender(path)
        except:
            pass
    def delete(self,index,files):
        index-=1
        current=files[index]
        path=str(current[-3])
        print("zzzzzzzzz",path)
        # ID  Type  Path  Size  Name
        try:
            useful.get_seekm(path)
            # self.transp.send(self.destip,(0,"get "+path))
        except:
            pass

    def ftp_client_page(self):
        print("qqqqqqqqqq")
        # gui.canvas["client"].pack_forget()
        # thr.join()
        print("kkkkkkkkkkk")
        self.transporter()
        temp=Canvas(gui.root,width=500,height=500)
        label=Label(temp,text="Clients File Options",font=("TimesNewRoman",30,"bold"),bg="#74e391",fg="#360809")
        temp.config(bg="#74e391")
        label.place(width=360,height=40,x=70,y=25)
        try:
            if (self.client.servers is not None) and self.destip in self.client.servers:
                self.desthost=self.client.servers[self.destip][0]
            elif((self.server.clients is not None) and (self.destip in self.server.clients)):
                self.desthost=self.server.clients[self.destip][0]

        except:
            print("Oh Fuckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        # print(555555550)
        # self.dest=self.answer[0]
        # self.destip=self
        tobe="Dest : "+str(self.destip)+"   "+str(self.desthost)
        print(tobe)
        Label(temp,text=tobe).place(x=0,y=0)
        # Label(temp,text="(Just Enter the number of your option)",font=("TimesNewRoman",10,"italic"),bg="#d6c187",fg="#360809").place(width=320,height=20,x=40,y=60)
        download=Button(temp,text="Download")
        # download.grid_location(x=50,y=50)
        download.place(x=60,y=450)
        listbox=Listbox(temp,width=25,height=8,background="#91dbbf",font=("Arial",15,"italic"),xscrollcommand=True,yscrollcommand=True)
        self.ls_otherside(temp)
        gui.canvas["ftpcli"]=temp
        # temp.pack()
    def flocker(self):#receiver
        print("->Kappa")
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.bind(("",2557))
        print("->Lamma")
        while True:
            print("8889999111000")
            k=s.recvmsg(1024)
            data=0
            print("Utaaaa")
            if(k != None):
                print("omega",k)
                data=k[0]
                
                data=pickle.loads(data)
                print("azita",data)
                self.dest=k[-1][0]
                self.destip=k[-1][0]
                self.answer=k[-1]

                s.close()
                break
        print("Sigma")
        self.ftp_client_page()
        print("Hmmmmmmmm....")
        self.canvas["client"].pack_forget()
        self.canvas["ftpcli"].pack()
    def listen_client_page(self):

        print("->Alpha")
        # gui.canvas["client"].pack_forget()
        t=threading.Thread(target=self.flocker)
        t.start()
        print("->Zeta")
        return t
            
    def switcher(self,dest:str):
        if("main" in dest):
            self.server.kill()
            self.server.socket.close()
        for i,j in gui.canvas.items():
            if(dest in i):
                j.pack()
            else:
                j.pack_forget()
    def ten(self,t):
        ip=useful.get_my_ip()
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        # s.bind(("",2557))
        data=pickle.dumps(t)
        # print("#########################################################",data)
        i=0
        for i in range(10):
            # print(self.server.ip)
            self.destip=self.dest
            s.sendto(data,(self.dest,2557))
            print("time:{}".format(i+1))
            import time
            time.sleep(2)
        # data=pickle.loads(data)
        
        # self.answer=data
        s.close()
    def returner(self,listi:dict,text):
        temp=[[i,j[0]] for i,j in listi.items()]

        f=False
        while(not f):
            try:
                current=int(text.get())
                f=True
            except:
                print("Not Valid")
        current-=1
        t=temp[current]
        # t=(t[0],self.desthost)
        print("Mockingbird",t)
        self.answer=t
        self.dest=t[0]
        self.destip=t[0]
        self.desthost=t[-1]
        print("else",self.desthost)
        
        threading.Thread(target=self.ten,args=[t]).start()

        self.ftp_server_page()
        # return t
    def rider(self):
        while True:
            if(len(self.server_ip_list)>0):
                gui.flag=False
                break
g=gui()