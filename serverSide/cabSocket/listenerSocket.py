'''
Created on Mar 25, 2016

@author: Mohammad Hashemi
'''
import threading
import socket
import json
from cabSocket.clientSocket import ClientSocketPassenger, ClientSocketDriver

class ListenerSocket:
    def __init__(self):
        self.__serversocket=None
        self.__listenerThread=None
    def __listen(self):
        self.__serversocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__serversocket.bind(('localhost', 20161))
        self.__serversocket.listen(10) #backlog is 10 
        BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
        while True:
            print "Waiting for a Client ..."
            conn, addr = self.__serversocket.accept()
            print 'Connection address:', addr
            data = conn.recv(BUFFER_SIZE)
            dataDict=json.loads(data)
            clientSock=None
            if 'appType' not in dataDict:
                raise "First msg Exception: there is no appType in recvd msg"
            if dataDict['appType']=='passenger':
                clientSock=ClientSocketPassenger()
            elif dataDict['appType']=='driver':
                clientSock=ClientSocketDriver()
            else:
                raise "appType has a problem!!!!"
            clientSock.setSocket(conn)
            print dataDict
                


    def runThread(self):
        self.__listenerThread=threading.Thread(target=self.__listen)
        self.__listenerThread.start()
        print "Listener thread is started."
        
