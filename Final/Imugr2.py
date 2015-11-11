#!/usr/bin/python2.7
# run as ./lecture17.py
# chmod +x lecture17.py in case its not executable
# use ls -al to see if file has an -x-

import sys, os, requests, urllib2, json, copy

class Battle(self):
	#Make an array of usernames
	userNames = ['LastAtlas', 'catslikecats', 'Tighe']

	for i in userNames:
		print "Username: " + i

	#userNamesDic = {}
	name_pic_points = [{} for x in range(0, len(userNames))]
	countj = 0
	#Loop through each username
	for i in userNames:
		#loop through each page count
		j = True
		page_num = 0
		while j == True:
			try: 
				#print countj
				userNameLink = "http://imgur.com/user/" + str(i) + "/index/newest/page/" + str(page_num) + "/hit.json?scrolling"
				response = urllib2.urlopen(userNameLink)
				data = response.read()
				if data == "":
					break
				jsonData = json.loads(data)
				#print userNameLink
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
					list_entry = {x: y}
					name_pic_points[countj].update(copy.copy(list_entry))			
					#print i, x, y
					countk = countk + 1
				except IndexError:
					break
			page_num +=  1
		countj = countj + 1
		

#print "***********************************"
#print name_pic_points[0]
#print name_pic_points[1]


	user_sets =[] #[set() for x in range(0, len(name_pic_points))]
	for user_dict in name_pic_points:
    	s = set(user_dict.keys())
    	user_sets.append(copy.copy(s))

	same_posts = set.intersection(*user_sets)

#print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
#print user_sets
#print "######################################"
#print same_posts

	post_points = []
	for s in same_posts:
		print "All users have commented on these posts: " + s
		for index in range(0, len(name_pic_points)):
			a = name_pic_points[index]
			b = a[s]
			post_points.append(b)
			index = index + 1

	l = 0
	for i in userNames:
		print "User " + str(i) + " has " + str(post_points[l]) + " points"
		l = l+1

	max_value = max(post_points)
	max_index = post_points.index(max_value)


	print "The winner is " + str(userNames[max_index])

