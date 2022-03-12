import socket
import time

eta = 120

msgFromClient       = "En route, ETA: "
bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024


# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
while eta > 0: 
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    time.sleep(3)
    eta = eta - 10


msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from RSU {}".format(msgFromServer[0])

print(msg)