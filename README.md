# 3D3_Project_1

This demo is a small scale example of the proposed Project. 
Each peer node represents a Road Side Unit(RSU) and the udp_client is out Emergancy vehicle. 
To set up the test, each peer is given its neighbours ip address and port number in a Distibuted Hash Table. Then each peer is run. 
The udp_client is given its path and the ip address for each peer. this code is then run.

Each peer should output the traffic direction that it is targeting and the travel route of the EV after it has passed the node.
The udp_peer should output when it has finished connection with a node.

References:
Code adapted partially from 
https://pythontic.com/modules/socket/udp-client-server-example
https://www.codeunderscored.com/socket-programming-in-python/#Example_3_UDP_Chating_System_Peer_to_Peer
