#!/usr/bin/python2.7
# run as ./lecture17.py
# chmod +x lecture17.py in case its not executable
# use ls -al to see if file has an -x-

import sys, os, requests, urllib2, json

#Make an array of usernames
userNames = ['LastAtlas', 'catslikecats', 'Tighe']
#userNamesDic = {}
name_pic_points = [[] for x in range(0, len(userNames))]



#Loop through each username
for i in userNames:
	#loop through each page count
	
	j = True
	countj = 0
	while j == True:
		try: 
			userNameLink = "http://imgur.com/user/" + str(i) + "/index/newest/page/" + str(countj) + "/hit.json?scrolling"
			response = urllib2.urlopen(userNameLink)
			data = response.read()
			jsonData = json.loads(data)
			
		except IndexError:
			break 
		except ValueError:
			break

		countk = 0
		k = True
		while k == True:
			#append the prints to new dictionsary
			try:
				x = jsonData['data']['captions']['data'][countk][u'hash']
				y =  jsonData['data']['captions']['data'][countk][u'points']
				#userNamesDic.update({i:[x,y]}) 
				name_pic_points[0].append(i)
				name_pic_points[1].append(x)
				name_pic_points[2].append(y)
							
				print i, x, y
				countk = countk +1
			except IndexError:
				break



		countj = countj + 1

print '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
print name_pic_points
#print dic_userName
#set dictionary here
#for i in dictionarArray:
	#










	#response = requests.get(userNameLink)
	#data = response.read()
	#jsonData = json.loads(data)
	#print jsonData

	#open Url of user name
	#loop through to scrape all the photo endings
		#create an array of all photo url endings

#should now have an n-arrays of photo endings for each username

#compare the three photo arrays (is there a dplyr like package) to make an new single array of the union

#loop through set photo arrary (Url path)
	#find user (loop through user array)
		#find the points, add it


#compare points

#json.loads(dictName)
#http://imgur.com/user/LastAtlas/index/newest/page/3/hit.json?scrolling
#obj["data"]
#obj["captions"]
#obb["data"]