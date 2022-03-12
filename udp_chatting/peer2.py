# peer2.py
# we are going to type the list in here

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
            print(data)
	


my_addr =('127.0.0.1',65431)
t_ip = '127.0.0.1' 
target =(t_ip, 65432)



s = socket(AF_INET, SOCK_DGRAM)
s.bind(my_addr)

print("waiting connection")

once = True

x = Thread(target=Receiving, args=(s, once))
x.start()

wel="OK!"
s.sendto(wel.encode('ascii'), target)

while True:
	msg = input("")
	s.sendto(msg.encode('ascii'), target)