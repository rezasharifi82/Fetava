def portal(ip,thing):
        port=3333
        """
        This is a sender method that must be threaded\n
        ipadd: ip address of the destination\n
        **port:** port number of the destination\n
        **object:** this one is compound\n
        -----
        object=(command:boolean to see whether is it command or object,command or object)
        command = 0:command 1:python_object 
        
        
        
        fheader(file size):file(we should put file s ize in the header)
        
        sata or thing:
        pwd: ("pwd",None)
        download : ("get" ,path)
        upload: ("send" , path)
        remove: ("rm", path)


        so for sending command:
        (0,("send",path))

        files:

        thing is 2D array (2,data)


        packet=(2,namefile,sedata)
        thing=()



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
        pickled=pickle.dumps(thing)
        s.sendall(pickled)
        s.close()

portal("192.168.1.107",(0,("pwd",0)))
# import os
# print(list(os.popen("pwd"))[0][:-1])