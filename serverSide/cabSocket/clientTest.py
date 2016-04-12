'''
Created on Apr 11, 2016

@author: incognito
'''
import socket
import json
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 20161))
firstMsg={"appType":"passenger","name":"Seyed"}

clientsocket.send(json.dumps(firstMsg))