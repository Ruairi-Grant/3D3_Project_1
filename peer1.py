# peer1.py
# Node C
from socket import *
from threading import *

def Receiving(sock,first_connect):
    while True:
        data, addr = sock.recvfrom(1024)
        if(first_connect and data.decode('ascii')=="OK!"):
            print("[+] Connected Successfully ")
            first_connect=False
            continue
        else:
            data = data.decode('ascii')
            
            nodes, eta = data.split('/')
            nodes = nodes.strip()
            nodes = nodes.split(' ')
            print("Travel Route: ", nodes, "\nETA to first node: ", eta)
            print("Start clearing traffic between", nodes[0], "and", nodes[1])
            if len(nodes)>2:
                target = node_table[nodes[1]]
                sock.sendto(data[1:].encode('ascii'), target)


my_addr = ('127.0.0.1', 65432)
t_ip= '127.0.0.1' 
#target=(t_ip, 65431)
node_table = {'B':(t_ip, 65431)}
s = socket(AF_INET,SOCK_DGRAM)
s.bind(my_addr)

print("Waiting Connection")

wel="OK!"
for key in node_table:
    target = node_table[key]
    s.sendto(wel.encode('ascii'), target)

first_connect = True
x = Thread(target=Receiving, args=(s,first_connect))
x.start()




    