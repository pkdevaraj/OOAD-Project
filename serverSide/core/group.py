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
        self.__driver.notify(msg)
    def notifyPassenger(self,passenger,msg):
        passenger.notify(msg)
    def terminate(self,summary):
#         ??????????
        pass
    def calculatePayment(self,summary):
#         ??????????
        pass
    def updateGroup(self,ttype,b):
#         What is type?
        pass
    def calculateFines(self,booking):
#         
        pass
    def updateDriver(self,driver, ttype):
#         I don't remember it!!!!
        pass
    def getPassengerSub(self):
        return self.__passengerSub
    def getDriverSub(self):
        return self.__driverSub
    def hasCancelled(self):
        if self.__cancelled==True:
            return True
        return False
    def isFull(self):
        if self.__full==True:
            return True
        return False
