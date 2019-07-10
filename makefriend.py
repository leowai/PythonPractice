__author__ = 'Administrator'
#conding = utf-8
import itchat
itchat.auto_login()
friends = itchat.get_friends(update=True)
#print (friends)