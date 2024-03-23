#Port 2273


def notification(message,title="Fetava"):
    from plyer import notification
    notification.notify(
        title = title,
        message = message,
        app_icon = "/usr/share/icons/Adwaita/22x22/devices/computer.png", #http://www.iconarchive.com/show/qetto-2-icons-by-ampeross/timer-icon.html
        timeout = 1,
    )
# def get_ip()-> list:
#     import os
#     p=(os.popen("arp").read())
#     import re
#     all_ip=re.findall("[1-9]{1,3}\.[1-9]{1,3}\.[1-9]{1,3}\.[1-9]{1,3}",p)
#     return all_ip
def generate_info():
    import socket
    host=socket.gethostname()
    import platform
    os_name=platform.system()
    di={"OS":os_name,"Name":host}
    return di
def welcome_pack_server():
    import socket
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    port=2273
    s.bind(("",port))
    # s.listen(5)
    return s

def welcome_pack_client():
    import socket
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    return s
def get_my_ip():
    import os
    command ='''
    ip addr | grep -Eo "[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}\/[0-9]{0,3}"|grep -Eo "[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}"
    '''
    p=[]
    for i in list(os.popen(command)):
        if((i.startswith("127")) or (i.startswith("10"))):
            pass
        else:
            p.append(i[:-1])
    return p[0]
def set_file(source=""):
    import os
    d=list(os.popen("pwd"))[0][:-1]
    # print(d)
    name=source.split("/")[-1]
    final=os.path.join(d,name)
    print("ofeta",d)
    os.system("cp {} {}".format(source,final))
def handshake(source=""):
    set_file(source)
def get_seekm(path=""):
    import os
    os.system("rm {}".format(path))
 
def get_all_files(path="./"):
    '''
    dir or file , path , size , name
    '''
    import os
    files=[]
    directories=[]
    alls=[]
    d=os.listdir(path)
    for i in d:
        pat=os.path.join(path,i)
        if(os.path.isfile(pat)):
            alls.append(("file",pat,os.path.getsize(pat),i))
            # print(os.path.getsize(pat))
        else:
            alls.append(("dir",pat,os.path.getsize(pat),i))
    return alls

def get_message(server_or_client=True) -> dict: #
    '''
    True if server and false if client\n
    @Fetava,Server,192.168.1.107,Lotova\n
    and return is not encoded\n
    IP\n
    hostname\n
    OS\n
    message
    '''
    di={}
    #@Fetava,Server,192.168.1.107,Lotova
    sep=","

    m="@Fetava"+sep
    if (server_or_client is True):
        m+="#Ser"+sep
    else:
        m+="#Cli"+sep
    m+=str(pol:=get_my_ip())+sep
    di["IP"]=pol
    kk=generate_info()
    di["hostname"]=kk["Name"]
    di["OS"]=kk["OS"]
    host=kk["Name"]
    os=kk["OS"] 
    m+=host
    di["message"]=m
    return di

# get_all_files()
# 
# def ask_out():
#     ip=get_ip()
#     class getit:
#         ips={i:0 for i in ip}
#     for i in ip:
#         pass
# get_seekm("./4")

# notification("fkadjgkd")
# print(get_message(False))