#!/usr/bin/python2.7
# run as ./lecture17.py
# chmod +x lecture17.py in case its not executable
# use ls -al to see if file has an -x-

import sys, os, requests, urllib2

#Make an array of usernames
userNames = ['LastAtlas', 'catslikecats', 'Tighe']


userNameLink = 'http://imgur.com/user/' + str(userNames[0])
response = requests.get(userNameLink)
print response.status_code





#Loop through each username
for i in userNames:
	print i
	#open Url of user name
	#loop through to scrape all the photo endings
		#create an array of all photo url endings

#should now have an n-arrays of photo endings for each username

#compare the three photo arrays (is there a dplyr like package) to make an new single array of the union

#loop through set photo arrary (Url path)
	#find user (loop through user array)
		#find the points, add it


#compare points