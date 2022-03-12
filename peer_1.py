##Connected to Peer 2 only
#taken from:
##https://python.hotexamples.com/examples/btpeer/BTPeer/-/python-btpeer-class-examples.html



from btpeer import *

peer1 = btpeer.BTPeer(5,25252, 1, "127.0.0.1")
peer2 = btpeer.BTPeer(5,15151, 2, "127.0.0.1")
t1 = threading.Thread(target = peer1.mainloop)
t2 = threading.Thread(target = peer2.mainloop)

m1 = 'hello from peer2'
m2 = 'HELLO FROM PEER1'
returns = {}

def handler1(peerconn, msgdata, returns=returns):
    print (peerconn, msgdata)
    returns['p1'] = msgdata
def handler2(peerconn, msgdata, returns=returns):
    print (peerconn, msgdata)
    returns['p2'] = msgdata

peer1.addhandler('HELL', handler1)
peer2.addhandler('HELL', handler2)

t1.start()
t2.start()

time.sleep(0.5)

peer1.connectandsend('localhost', 25252, 'HELL', m2)
peer2.connectandsend('localhost', 15151, 'HELL', m1)

time.sleep(0.1)

unittest.assertEqual(returns['p1'], m1)
unittest.assertEqual(returns['p2'], m2)

peer1.shutdown = True
peer2.shutdown = True
# motivate threads to exit
try:
    c = btpeer.BTPeerConnection(None, 'localhost', 15151)
    c.close()
except socket.error:
    pass
try:
    c = btpeer.BTPeerConnection(None, 'localhost', 25252)
    c.close()
except socket.error:
    pass