'''
Created on Mar 25, 2016

@author: Mohammad Hashemi
'''
class Booking:
    def __init__(self,passenger,pickup,dropoff,time,rating,shared,accomp,grp):
        self.__refID=None
        self.__passenger=passenger
        self.__pickupLocation=pickup
        self.__dropoffLocation=dropoff
        self.__timeInterval=time
        self.__rating=rating
        self.__sharedWith=shared
        self.__accompanyingWith=accomp
        self.__gid=grp
    def getBookingDetails(self):
        res={}
        res['refID']=self.__refID
        res['passenger']=self.__passenger
        res['pickupLocation']=self.__pickupLocation
        res['dropoffLocation']=self.__dropoffLocation
        res['timeInterval']=self.__timeInterval
        res['rating']=self.__rating
        res['sharedWith']=self.__sharedWith
        res['accompanyingWith']=self.__accompanyingWith
        res['gid']=self.__gid
    def getTimeInterval(self):
        return self.__timeInterval
    def getPassenger(self):
        return self.__passenger
    def getPickupAndDropoff(self):
        PDTouple =(self.__pickupLocation,self.__dropoffLocation)
        return PDTouple
    def updateGroupID(self,ID):
        self.__gid=ID
    