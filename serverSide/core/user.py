'''
Created on Mar 25, 2016

@author: Mohammad Hashemi
'''
from abc import ABCMeta, abstractmethod
import Booking
import smtplib

from core import CabSharing

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
        self.__bah=None
    def notify(self,msg):
        self.__cs.send(msg)
        pass
    def verifyPaymentProfile(self):
        return True
        pass
    def addPaymentProfile(self,profile):
        self.__bah = profile
        pass
    def getUserName(self):
        return self.__userName
        pass
    def sendEmail(self,msg):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("Your Email", "YOUR PASSWORD")
        server.sendmail("Your Email", self.__email, msg)
        server.quit()
        pass
    def removeUser(self):
        self.__cs.deleteUser()
        pass
    def getBankAccountHandler(self):
        return self.__bah
        pass
    
class Passenger(User):
    
    def __new__(self, *args, **kwargs):
        return object.__new__(self, *args, **kwargs)
    def __init__(self,name,socket,email,profile):
        super(Passenger, self).__init__(name,socket,email,profile)
        self.__bookings=None
    def provideFeedback(self,comment,rating, booking):
        bookings = self.getAllBookings(self)
        for book in bookings:
            if book.__gid == booking:
                groupId = book.__groupID
                cs = CabSharing()#singleton object how to access
                group = cs.getGroupFromID(cs, groupId)      
                driver = group.getDriverSub(group)
                driver.addComment(driver, comment)
                driver.updateRatings(driver, rating)
                
        pass
    def bookCab(self,bookingPref):
        cs = CabSharing()#singleton object how to access
        passenger = bookingPref['passenger']
        pickup = bookingPref['pickup']
        dropoff = bookingPref['dropoff']
        time = bookingPref['time']
        rating = bookingPref['rating']
        shared = bookingPref['shared']
        accomp = bookingPref['accomp']
        grp = bookingPref['grp']
        booking = Booking(self,passenger,pickup,dropoff,time,rating,shared,accomp,grp)
        cs.addBookingToGrid(cs, booking)
        self.__bookings.append(booking)
        pass
    def cancelCab(self,bID):
        cs = CabSharing()#singleton object how to access
        cs.cancelBooking(cs, bID)
        pass
    def getAllBookings(self):
        return self.__bookings
        pass


class Driver(User):
    
    def __new__(self, *args, **kwargs):
        return object.__new__(self, *args, **kwargs)
    def __init__(self,name,socket,email,profile):
        super(Driver, self).__init__(name,socket,email,profile)
        self.__license=None
        self.__rating=0
        self.__ratingCount=0
        self.__cmnts=[]
        self.__groups=None
        self.__homeLocation=None
    def selectGroup(self,ID):
        
        pass
    def cancelGroup(self,ID):
        pass
    def updateRatings(self,newRate):
        self.__rating = self.__rating + newRate
        self.__ratingCount = self.__ratingCount+1
        pass
    def addComment(self,cmnt):
        self.__cmnts.append(cmnt)
        pass
    def endTrip(self,travelSummary):   
        cs = CabSharing()#singleton object how to access
        cs.endTrip(cs, travelSummary)
        pass
    def getRating(self):
        return int(self.__rating/self.__ratingCount)
        pass
    def getLicense(self):
        return self.__license
        pass
    def getComments(self):
        return self.__cmnts
        pass
    def getDriverGroups(self):
        pass
    def addDriverGroup(self,grp):
        pass
    def getHomeLocation(self):
        return self.__homeLocation
        pass
    def setLicense(self,llicense):
        self.__license = llicense
        pass
    def setHomeLocation(self,home):
        self.__homeLocation = home
        pass
    def getMyCurrentLocation(self):
        return self.__homeLocation
        pass
    

    
    
# pp=Passenger("hasan",2,3,4)
# print pp.getUserName()
#         