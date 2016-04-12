'''
Created on Mar 25, 2016

@author: Mohammad Hashemi
'''
import pymongo
from pymongo.mongo_client import MongoClient
from __builtin__ import dict
class DBManager:
    def __init__(self):
        self.__mongoClient=None
        self.__db=None
    def connect(self):
        print "Connecting to DB ..."
        self.__mongoClient  = MongoClient()
        self.__db = self.__mongoClient['cabSharing']
        
    def get(self,query,dbname):
        doc=None
        if type(query)!=dict:
            raise "Exception: query should be a dictionary"
        if dbname=='users':
            doc=self.__db.users.find_one(query)
        elif dbname=='bookings':
            doc=self.__db.bookings.find_one(query)
        return doc
            
    
    def update(self,filter,query,dbname):
        if type(query)!=dict:
            raise "Exception: query should be a dictionary"
        if dbname=='users':
            self.__db.users.update_one(filter,{"$set":query})
        elif dbname=='bookings':
            self.__db.bookings.update_one(filter,{"$set":query})
        
    def insert(self,query,dbname):
        if type(query)!=dict:
            raise "Exception: query should be a dictionary"
        if dbname=='users':
            self.__db.users.insert_one(query)
        elif dbname=='bookings':
            self.__db.bookings.insert_one(query)
        
    
    
# if __name__=="__main__":
#     print "Testing DB ..."
#     dbm=DBManager()
#     dbm.connect()
#     query={"username":"mohammad","password":"abcd"}
#     dbm.insert(query,'users')
#     query={"username":"praveen","password":"cccc"}
#     dbm.insert(query,'users')
#     query={"username":"nach","password":"ccc"}
#     dbm.insert(query,'users')
#     print "end of inserting..."
#     query ={"username":"mohammad"}
#     print dbm.get(query, "users")
#     query ={"username":"nachi"}
#     print dbm.get(query, "users")
#     query ={"username":"nach"}
#     print dbm.get(query, "users")
#     query ={"username":"praveen"}
#     print dbm.get(query, "users")
#     print 'end of getting...'
#     print ''
#     query={"password":"9876"}
#     filter={'username':'mohammad'}
#     dbm.update(filter,query,'users')
#     query={"username":"mohammad"}
#     print dbm.get(query,'users')
#     
    
    