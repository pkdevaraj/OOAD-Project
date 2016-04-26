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
        
    def verifyPaymentProfile(self):
        return True
        
    def addPaymentProfile(self,profile):
        self.__bah = profile
        
    def getUserName(self):
        return self.__userName
        
    def sendEmail(self,msg):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("Your Email", "YOUR PASSWORD")
        server.sendmail("Your Email", self.__email, msg)
        server.quit()
        
    def removeUser(self):
        self.__cs.deleteUser()
        
    def getBankAccountHandler(self):
        return self.__bah

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
                cs = CabSharing()#singleton 
                group = cs.getGroupFromID(cs, groupId)      
                driver = group.getDriverSub(group)
                driver.addComment(driver, comment)
                driver.updateRatings(driver, rating)
                
    def bookCab(self,bookingPref):
        cs = CabSharing()#singleton 
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
        
    def cancelCab(self,bID):
        cs = CabSharing()#singleton
        cs.cancelBooking(cs, bID)
        
    def getAllBookings(self):
        return self.__bookings
        
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
        
    def addComment(self,cmnt):
        self.__cmnts.append(cmnt)
        
    def endTrip(self,travelSummary):   
        cs = CabSharing()#singleton 
        cs.endTrip(cs, travelSummary)
        
    def getRating(self):
        return int(self.__rating/self.__ratingCount)
        
    def getLicense(self):
        return self.__license
        
    def getComments(self):
        return self.__cmnts
        
    def getDriverGroups(self):
        pass
    def addDriverGroup(self,grp):
        pass
    def getHomeLocation(self):
        return self.__homeLocation
        
    def setLicense(self,llicense):
        self.__license = llicense
        
    def setHomeLocation(self,home):
        self.__homeLocation = home
        
    def getMyCurrentLocation(self):
        return self.__homeLocation

# pp=Passenger("hasan",2,3,4)
# print pp.getUserName()
#         