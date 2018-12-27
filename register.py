#!/usr/bin/python3
import pyrebase	
import serial
rf = serial.Serial('/dev/ttyUSB0')
#Firebase Configuration

config = {
  "apiKey":"AIzaSyBeTkzdsVpcKpZkU9BMzNwCloUlNf2MWAo",
  "authDomain": "eventmanager-54b85.firebaseapp.com",
  "databaseURL": "https://eventmanager-54b85.firebaseio.com",
  "storageBucket": "eventmanager-54b85.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
while 1:
	a = input("enter the user ID number : ")
	s = rf.read(12)
	temp = str(s)
	db.child("passCods").child(a).set(temp)
	c = db.child("passCods").child(a).get()
	print(c.val())
