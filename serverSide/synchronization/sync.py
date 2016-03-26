'''
Created on Mar 25, 2016

@author: Mohammad Hashemi
'''
import thread
import threading
import types
import time

def synchronized_with_attr(lock_name):
    
    def decorator(method):
            
        def synced_method(self, *args, **kws):
            lock = getattr(self, lock_name)
            with lock:
                return method(self, *args, **kws)
                
        return synced_method
        
    return decorator

    
def syncronized_with(lock):
    
    def synchronized_obj(obj):
        
        if type(obj) is types.FunctionType:
#             print "ccc",obj
            obj.__lock__ = lock
            
            def func(*args, **kws):
                with lock:
                    return obj(*args, **kws)
            return func
            
        elif type(obj) is types.ClassType:
            
            orig_init = obj.__init__
            def __init__(self, *args, **kws):
                self.__lock__ = lock
                orig_init(self, *args, **kws)
            obj.__init__ = __init__
            
            for key in obj.__dict__:
                val = obj.__dict__[key]
                if type(val) is types.FunctionType:
                    decorator = syncronized_with(lock)
                    obj.__dict__[key] = decorator(val)
            
            return obj
    
    return synchronized_obj
    
    
def synchronized(item):
    if type(item) is types.StringType:
        decorator = synchronized_with_attr(item)
        return decorator(item)
    
    if type(item) is thread.LockType:
        decorator = syncronized_with(item)
        return decorator(item)
        
    else:
        new_lock = threading.Lock()
        decorator = syncronized_with(new_lock)
        return decorator(item)
    
   
   
   
   
################### Example of Synchronized ################# 
# @synchronized
# class Counter:
#     
#     def __init__(self):
#         self.counter = 0
# #         self.counter1 = 0
# #         self.counter2 = 0
#         
# #     @synchronized
#     def add_one(self):
#         val = self.counter
#         val += 1
#         time.sleep(0.1)
#         self.counter = val
# #         self.counter1+=1
# #         print "one",self.counter1
#         
#         
# #     @synchronized
#     def add_two(self):
#         print "two"
#         val = self.counter
#         val += 2
# #         time.sleep(0.1)
# #         self.counter = val
#         
# 
# def class_counter1():
#     global my_counter
#     for i in range(0,10): 
#         my_counter.add_one()
# #         time.sleep(0.01)
#     
# def class_counter2():
#     global my_counter
#     for i in range(0,10): my_counter.add_two()
# 
# if __name__ == '__main__':
#     my_counter = Counter()
#     thread1 = threading.Thread(target = class_counter1)
#     thread2 = threading.Thread(target = class_counter2)
#     
#     thread1.start()
#     thread2.start()
#     
#     thread1.join()
#     thread2.join()
#     
#     print my_counter.counter
################### End of Example of Synchronized #################