'''
Created on Mar 25, 2016

@author: Mohammad Hashemi
'''
import sys
print sys.path
from synchronization.sync import synchronized
class CabSharing(object):
    __instance=None
    
    #singleton design pattern
    @synchronized
    def __new__(cls, *args, **kwargs):
            if not cls.__instance:
                cls.__instance = super(CabSharing, cls).__new__(cls, *args, **kwargs)
                print cls.__instance
            return cls.__instance
    #constructor
    def __init__(self):
        self.__users={}
        self.__bookingGrid=None
        self.__driverGrid=None
        self.__cancelledBookings={}
        self.__groups={}
        self.__bookingEventList=None
        self.__cancelledEventList=None
        self.__listenerThread=None
        self.__bookingHandlerThread=None
        self.__cancellingHandlerThread=None
        self.__db=None
    def init(self):
        pass
    def listener(self):
        pass
    def matchGroup(self,booking):
        pass
    def addBookingToGrid(self,booking):
        pass
    def cancelBooking(self,bID):
        pass
    def __broadcastGroup(self):
        pass
    def endTrip(self,summary):
        pass
    def __bookingEventHandler(self):
        pass
    def cancellingEventHandler(self):
        pass
    def __addToEventList(self,ttype,booking):
        pass
    def __removeFromEventList(self,ttype,booking):
        pass
    def getDB(self):
        pass
    def getUserFromID(self,ID):
        pass
    def getGroupFromID(self,ID):
        pass
    
        
if __name__ == '__main__':
    print "server is started ..."
    pass
#     print "qq"
#     s1 = CabSharing()
#     print "main",s1
#     print s1.__
#     print s1.addBookingToGrid(2)
    
#     s2 = CabSharing()
#     if (id(s1) == id(s2)):
#         print "Same"
#     else:
#         print "Different"
