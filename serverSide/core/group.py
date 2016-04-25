'''
Created on Mar 25, 2016

@author: Mohammad Hashemi
'''
class Group:
    def __init__(self,grp,dur,distance,esti,time):
        self.__groupID=grp
        self.duration=dur
        self.__bookings=None
        self.__distance=distance
        self.__estimatedCost=esti
        self.__full=None
        self.__driver=None
        self.__timeInterval=time
        self.__passengerSub=None
        self.__driverSub=None
        self.__cancelled=None
        
    def notifyDriver(self,msg):
        pass
    def notifyPassenger(self,passenger,msg):
        pass
    def terminate(self,summary):
        pass
    def calculatePayment(self,summary):
        pass
    def updateGroup(self,ttype,b):
        pass
    def calculateFines(self,booking):
        pass
    def updateDriver(self,driver, ttype):
        pass
    def getPassengerSub(self):
        pass
    def getDriverSub(self):
        return self.__driver()
        pass
    def hasCancelled(self):
        pass
    def isFull(self):
        pass