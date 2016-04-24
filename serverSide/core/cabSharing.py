'''
Created on Mar 25, 2016

@author: Mohammad Hashemi
'''
from synchronization.sync import synchronized
from handler.DBManager import DBManager
from cabSocket.listenerSocket import ListenerSocket
import math
import json
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
        self.__PbookingGrid=None #pick up booking grid
        self.__DbookingGrid=None #drop off booking grid
        self.__driverGrid=None
        self.__cancelledBookings={}
        self.__groups={}
        self.__bookingEventList=[]
        self.__cancelledEventList=[]
        self.__listenerSocket=ListenerSocket()
        self.__bookingHandlerThread=None
        self.__cancellingHandlerThread=None
        self.__db=DBManager()
    def init(self):
        print("connecting to database...")
        self.__db.connect()
        print("load all users from db... (Not working)")
        # TODO: load all users from db and create User objects
        print ("Starting listener socket ...")
        self.__startlistener()
        # TODO: implement listenerSocket class
        
        
        
    def __startlistener(self): #old method name: listener
        self.__listenerSocket.runThread()
    def matchGroup(self,booking):
        pass
    def addBookingToGrid(self,booking):
        (pickup,dropoff)=booking.getPickupAndDropoff()
        
        """
        40.01047, -105.2736   <<< ---- >>> 40.02047, -105.2836
                x between 35 to 45
                y between -110 to -100 
        """

        index1=int(math.floor((pickup[0]-35)*100))
        index2=int(math.floor((pickup[1]+110)*100))
        self.__PbookingGrid[index1][index2].append(booking)
        
        index1=int(math.floor((dropoff[0]-35)*100))
        index2=int(math.floor((dropoff[1]+110)*100))
        self.__DbookingGrid[index1][index2].append(booking)
        
    
    def __broadcastGroup(self,group):
        msg=json.dumps(group.getGroupDetails())
        for d in self.__driverGrid:
            d.notify(msg)
    def endTrip(self,summary):
        pass
    def __bookingEventHandler(self):
        pass
   
    def __addToEventList(self,ttype,booking):
        if ttype=='booking':
            self.__bookingEventList
        pass
    def __removeFromEventList(self,ttype,booking):
        pass
    def getDB(self):
        return self.__db
    def getUserFromID(self,ID):
        return self.__users[ID]
    def getGroupFromID(self,ID):
        return self.__groups[ID]
    def cancelBooking(self,bID):
        #no need to be implemented
        pass
    def cancellingEventHandler(self):
        #no need to be implemented
        pass
        
if __name__ == '__main__':
    print "server is started ..."
    cs=CabSharing()
    cs.init()
    print "done"
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
