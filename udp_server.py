import socket

localIP     = "127.0.0.2"
localPort   = 20001
bufferSize  = 1024

msgFromServer       = "Message received."
bytesToSend         = str.encode(msgFromServer)
 
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("RSU 1 online.")

# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    address = bytesAddressPair[1] # in case we want to send a message back to the EV, e.g. a confirmatory message

    clientMsg = "EV inbound - {}".format(message)
    
    print(clientMsg)