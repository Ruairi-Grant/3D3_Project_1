# peer1.py
from socket import *
from threading import *

def Receiving(sock,first_connect):
    while True:
        data, addr = sock.recvfrom(1024)
        if(first_connect and data.decode('ascii')=="OK!"):
            print("[+] Connected Successfully ")
            wel="OK!"
            sock.sendto(wel.encode('ascii'), target)
            first_connect=False
            continue
        else:
            data = data.decode('ascii')
            print(data)
            sock.sendto(data[1:].encode('ascii'), target)
            #nodes, eta = data.split('/')
            #print(nodes, eta)

my_addr = ('127.0.0.1', 65432)
t_ip= '127.0.0.1' 
target=(t_ip, 65431)
s = socket(AF_INET,SOCK_DGRAM)
s.bind(my_addr)

print("Waiting Connection")

wel="OK!"
s.sendto(wel.encode('ascii'), target)

first_connect = True
x = Thread(target=Receiving, args=(s,first_connect))
x.start()

while True:
    msg = input("")
    s.sendto(msg.encode('ascii'), target)


    