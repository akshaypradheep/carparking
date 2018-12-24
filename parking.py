#!/usr/bin/python3
import pyrebase
busRoute = "chkra-thrissur"
#Firebase Configuration
config = {
  #"apiKey": "vfUtznfQTNsjBnwNw5VTrNEldJVydp5CgNMfTjk5",
  "apiKey":"AIzaSyBeTkzdsVpcKpZkU9BMzNwCloUlNf2MWAo",
  "authDomain": "akshaypradheepdc.firebaseapp.com",
  "databaseURL": "https://akshaypradheepdc.firebaseio.com",
  "storageBucket": "akshaypradheepdc.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

a = db.child("passCodes").get()
newdict = a.val()
newlist = list()
for key in newdict.keys():
  print(key)
  newlist.append(key)
_pass = list()
for i in newlist:
	print (newdict[i])

	