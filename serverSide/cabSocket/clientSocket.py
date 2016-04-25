'''
Created on Mar 25, 2016

@author: Mohammad Hashemi
'''
from abc import ABCMeta, abstractmethod
import threading
import socket
import json

from core.user import Passenger, Driver


class ClientSocket:
    __metaclass__ = ABCMeta
    def __init__(self):
        self.__user=None
        self.__socket=None
        self.__receiverThread=threading.Thread(target=self.__receive)
        self.__receiverThread.start()
        print "Reciever thread is started."
        
        
    def __receive(self):
        #self.__socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.__socket.bind(('localhost', 20161))
        #self.__socket.listen(10) #backlog is 10 
        BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
        while True:
            print "Waiting for a Client ..."
            conn, addr = self.__socket.accept()
            print 'Connection address:', addr
            data = conn.recv(BUFFER_SIZE)
            dataDict=json.loads(data)
            print dataDict
            self.parseCommands(self, dataDict)
        pass

    def send(self,msg):
        totalsent = 0
        MSGLEN = len(msg)
        while totalsent < MSGLEN:
            sent = self.__socket.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent
        pass

    def getSocket(self):
        return self.__socket
        pass

    def setSocket(self,socket):
        self.__socket = socket
        pass

    @abstractmethod
    def parseCommands(self,query):
        pass

    @abstractmethod
    def signup(name, self, email, userProfile):
        pass

    def login(self,ID,password):
        pass

    def logout(self):
        pass
    
    def deleteUser(self):
        del self.__user

class ClientSocketPassenger(ClientSocket):    

    def parseCommands(self, query):
        ClientSocket.parseCommands(self, query)
        if query['function']=='login' and 'Id' in query and 'password' in query:
            ClientSocket.login(ClientSocket, query['Id'], query['password'])
        if query['function']=='logout':
            ClientSocket.logout(ClientSocket)
        if query['function']=='singup':
            name = ""
            email = ""
            userProfile = {}
            if 'name' in query:
                userProfile = query['name']
            if 'email' in query:
                userProfile = query['email']
            if 'userProfile' in query:
                userProfile = query['userProfile']
                
            ClientSocket.singup(name, ClientSocket, email, userProfile)
        pass

    def signup(name, self, email, userProfile):
        ClientSocket.signup(self, userProfile)
        ClientSocket.__user = Passenger(name, self, email, userProfile)        
        pass
    
class ClientSocketDriver(ClientSocket):    

    def parseCommands(self, query):
        ClientSocket.parseCommands(self, query)
        if query['function']=='login' and 'Id' in query and 'password' in query:
            ClientSocket.login(ClientSocket, query['Id'], query['password'])
        if query['function']=='logout':
            ClientSocket.logout(ClientSocket)
        if query['function']=='singup':
            name = ""
            email = ""
            userProfile = {}
            if 'name' in query:
                userProfile = query['name']
            if 'email' in query:
                userProfile = query['email']
            if 'userProfile' in query:
                userProfile = query['userProfile']
            ClientSocket.singup(name, ClientSocket, email, userProfile)
            
        if query['function']=='endTrip':
            self.__user.endTrip(self, query['travelSummary'])
        if query['function']=='cancelGroup':
            self.__user.cancelGroup(self, query['id'])
        if query['function']=='selectGroup':
            self.__user.selectGroup(self, query['id'])
        if query['function']=='setHomeLocation':
            self.__user.setHomeLocation(self, query['homelocation'])
        pass

    def signup(name, self, email, userProfile):
        ClientSocket.signup(self, userProfile)
        ClientSocket.__user = Driver(name, self, email, userProfile)
        pass
