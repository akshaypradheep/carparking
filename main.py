#!/usr/bin/python3
import pyrebase
import serial
rf = serial.Serial('/dev/ttyUSB0')
#Firebase Configuration


config = {
  #"apiKey": "vfUtznfQTNsjBnwNw5VTrNEldJVydp5CgNMfTjk5",
  "apiKey":"AIzaSyBeTkzdsVpcKpZkU9BMzNwCloUlNf2MWAo",
  "authDomain": "eventmanager-54b85.firebaseapp.com",
  "databaseURL": "https://eventmanager-54b85.firebaseio.com",
  "storageBucket": "eventmanager-54b85.appspot.com"
}
#https://eventmanager-54b85.firebaseio.com/


firebase = pyrebase.initialize_app(config)
db = firebase.database()

while True:
	s = rf.read(12)
	temp = str(s)
	a = db.child(temp).get()
	check = a.val()
	if check == "1":
		print("access granted")
		db.child(temp).set("0")
		pass
	if check == "0":
		print("you have already used")
		pass
	pass