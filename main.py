import fbchat
from fbchat import Client
from getpass import getpass
username = "Gabriel"
client = fbchat.Client(username, getpass())
no_of_friends = int(input("Number of friends: "))
for i in range(no_of_friends):
    name = str(input("Name: "))