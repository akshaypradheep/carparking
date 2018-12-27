#!/usr/bin/python3
import pyrebase
#Firebase Configuration

#config = {
#  #"apiKey": "vfUtznfQTNsjBnwNw5VTrNEldJVydp5CgNMfTjk5",
#  "apiKey":"AIzaSyBeTkzdsVpcKpZkU9BMzNwCloUlNf2MWAo",
#  "authDomain": "akshaypradheepdc.firebaseapp.com",
#  "databaseURL": "https://akshaypradheepdc.firebaseio.com",
#  "storageBucket": "akshaypradheepdc.appspot.com"
#}
config = {
  "apiKey":"AIzaSyBeTkzdsVpcKpZkU9BMzNwCloUlNf2MWAo",
  "authDomain": "eventmanager-54b85.firebaseapp.com",
  "databaseURL": "https://eventmanager-54b85.firebaseio.com",
  "storageBucket": "eventmanager-54b85.appspot.com"
}
#https://eventmanager-54b85.firebaseio.com/


firebase = pyrebase.initialize_app(config)
db = firebase.database()

a = db.child("eventgust").get()
pas = list()
newdict = a.val()
for key in newdict.values():
#	print(key)
	pas.append(key)
for i in pas:
	_usr = str(i)
	db.child(_usr).set("1")