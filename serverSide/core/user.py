'''
Created on Mar 25, 2016

@author: Mohammad Hashemi
'''
from abc import ABCMeta, abstractmethod

class User(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def __new__(self, *args, **kwargs):
        pass
    def __init__(self,name,socket,email,profile):
        self.__userName=name
        self.__cs=socket
        self.__bah=None
        self.__email=email
        self.__status=None
    def notify(self,msg):
        pass
    def verifyPaymentProfile(self):
        pass
    def addPaymentProfile(self,profile):
        pass
    def getUserName(self):
        return self.__userName
        pass
    def sendEmail(self,msg):
        pass
    def removeUser(self):
        pass
    def getBankAccountHandler(self):
        pass
    
class Passenger(User):
    
    def __new__(self, *args, **kwargs):
        return object.__new__(self, *args, **kwargs)
    def __init__(self,name,socket,email,profile):
        super(Passenger, self).__init__(name,socket,email,profile)
        self.__bookings=None
    def provideFeedback(self,comment,rating):
        pass
    def bookCab(self,bookingPref):
        pass
    def cancelCab(self,bID):
        pass
    def getAllBookings(self):
        pass


class Driver(User):
    
    def __new__(self, *args, **kwargs):
        return object.__new__(self, *args, **kwargs)
    def __init__(self,name,socket,email,profile):
        super(Driver, self).__init__(name,socket,email,profile)
        self.__license=None
        self.__rating=None
        self.__ratingCount=None
        self.__cmnts=None
        self.__groups=None
        self.__homeLocation=None
    def selectGroup(self,ID):
        pass
    def cancelGroup(self,ID):
        pass
    def updateRatings(self,newRate):
        pass
    def addComment(self,cmnt):
        pass
    def endTrip(self,travelSummary):
        pass
    def getRating(self):
        pass
    def getLicense(self):
        pass
    def getComments(self):
        pass
    def getDriverGroups(self):
        pass
    def addDriverGroup(self,grp):
        pass
    def getHomeLocation(self):
        pass
    def setLicense(self,llicense):
        pass
    def setHomeLocation(self,home):
        pass
    def getMyCurrentLocation(self):
        pass
    

    
    
# pp=Passenger("hasan",2,3,4)
# print pp.getUserName()
#         