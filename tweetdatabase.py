# (c) anupamkumar08 --->https://github.com/anupamkumar08
import tweepy
import time
import os, random 

ckey='add consumer key'
csecret='consumer secret'
akey='access token'
asecret='access secret'

auth=tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(akey, asecret)
x=1  
file = open('ur file in which contents are listed','r')
for line in file :
        s = line 
	api=tweepy.API(auth)
	api.update_status(status=s)
	time.sleep(5) #as per convinience
