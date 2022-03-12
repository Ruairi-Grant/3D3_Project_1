import socket
import time

eta = 120

serverAddressPort   = ("127.0.0.2", 20001)
bufferSize          = 1024

# Path planning algorithm will be implemented here to generate a list of nodes along the EV's route
def generate_node_list():
    return ("A B C D E /")

# ETA calculating algoritm will be implemented here
#def return_eta():
#    return(0)

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
while eta > 0:
    node_list = generate_node_list()
    converted_eta = str(eta)
    msgFromClient = node_list + converted_eta
    bytesToSend = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    time.sleep(3)
    eta = eta - 10

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from RSU {}".format(msgFromServer[0])

print(msg)