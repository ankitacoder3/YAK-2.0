import os
import pika 
import sys
import socket
import time

  





def check(top,msg):
    p = ""
    path=os.path.join(p,top)
    fn=top+".txt"

    print(path)
    if(os.path.exists(path)):
        print("Directory already exists")
        with open(os.path.join(path, fn), 'a') as fp:
            fp.write(msg+"\n")
            fp.close()
                                  


    else:
        os.makedirs(path)
        print("Directory created")
        with open(os.path.join(path, fn), 'w') as fp:
            fp.write(msg+"\n")
            fp.close()
            

def read_brok(top):
    p = ""
    path=os.path.join(p,top)
    fn=top+".txt"
    file1 = open(os.path.join(path, fn), "r+")
    print(file1.read())

    


ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004
print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ClientMultiSocket.recv(1024)
while True:
    
    Input = 'Broker connected'
    ClientMultiSocket.send(str.encode(Input))
    time.sleep(5)
ClientMultiSocket.close()