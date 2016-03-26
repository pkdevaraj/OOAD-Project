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
        pass
    def getTimeInterval(self):
        pass
    def getPassenger(self):
        pass
    def getPickupAndDropoff(self):
        pass
    def updateGroupID(self,ID):
        pass
    