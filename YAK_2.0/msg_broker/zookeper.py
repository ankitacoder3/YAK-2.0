import socket
import os
from _thread import *
import time
import subprocess
import random

broker_id=random.sample(range(1, 100), 3)
broker_array=['broker1.py','broker2.py','broker3.py']

max_index=broker_id.index(max(broker_id))
broker_id.pop(max_index)
maxindex_broker=broker_array.pop(max_index)



ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Zookeeper started..')
ServerSideSocket.listen(5)
def multi_threaded_client(connection):
    connection.send(str.encode('Zookeeper is working:'))
    while True:
        
        data = connection.recv(2048)
        print(data.decode('utf-8'))
        #response = 'Server message: ' + data.decode('utf-8')
        response = 'Zookeeper is listening'
        if not data:
            print("Didnt receive data")
            break
        connection.sendall(str.encode(response))
        time.sleep(5)
    connection.close()
while True:
    
    
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()