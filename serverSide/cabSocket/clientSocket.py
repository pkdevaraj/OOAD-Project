'''
Created on Mar 25, 2016

@author: Mohammad Hashemi
'''
from abc import ABCMeta, abstractmethod

class ClientSocket:
    __metaclass__ = ABCMeta
    def __init__(self):
        self.__user=None
        self.__socket=None
        self.__receiverThread=None
    def __receive(self):
        pass
    def send(self,msg):
        pass
    def getSocket(self):
        pass
    def setSocket(self,socket):
        pass
    @abstractmethod
    def parseCommands(self,query):
        pass
    @abstractmethod
    def signup(self,userProfile):
        pass
    def login(self,ID,password):
        pass
    def logout(self):
        pass

class ClientSocketPassenger(ClientSocket):    
    def parseCommands(self, query):
        ClientSocket.parseCommands(self, query)
        pass
    def signup(self, userProfile):
        ClientSocket.signup(self, userProfile)
        pass
    
class ClientSocketDriver(ClientSocket):    
    def parseCommands(self, query):
        ClientSocket.parseCommands(self, query)
        pass
    def signup(self, userProfile):
        ClientSocket.signup(self, userProfile)
        pass
    
