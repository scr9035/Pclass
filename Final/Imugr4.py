#!/usr/bin/python2.7
# run as ./lecture17.py
# chmod +x lecture17.py in case its not executable
# use ls -al to see if file has an -x-

'''Scr9035 Final. Input user names and find out
who or is it whom, is the biggest imgur
Karma Whore. Run the program in the terminal
to see the magic happyn. Whoa, look how he
spelled happyn. I should copywrite that and
create an app.'''

import sys, os, requests, urllib2, json, copy


STRING_INPUT = raw_input("Input Usernames here seperated by a space: ")
USERNAMES = STRING_INPUT.split()
USERNAMES = [str(a) for a in USERNAMES]
#print USERNAMES
#Make an array of usernames
#userNames = ['LastAtlas', 'catslikecats', 'Tighe']

for i in USERNAMES:
    print "Username: " + i

#userNamesDic = {}
NAME_PIC_POINTS = [{} for x in range(0, len(USERNAMES))]



COUNTJ = 0
#Loop through each username
for i in USERNAMES:
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
                y = jsonData['data']['captions']['data'][countk][u'points']
                list_entry = {x: y}
                NAME_PIC_POINTS[COUNTJ].update(copy.copy(list_entry))
                #print i, x, y
                countk = countk + 1
            except IndexError:
                break
        page_num = page_num + 1
    COUNTJ = COUNTJ + 1
#print "***********************************"
#print name_pic_points[0]
#print name_pic_points[1]


USER_SETS = [] #[set() for x in range(0, len(name_pic_points))]
for user_dict in NAME_PIC_POINTS:
    s = set(user_dict.keys())
    USER_SETS.append(copy.copy(s))

SAME_POSTS = set.intersection(*USER_SETS)

#print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
#print user_sets
#print "######################################"
#print same_posts

POST_POINTS = []
for s in SAME_POSTS:
    print "All users have commented on these posts: " + s
    for index in range(0, len(NAME_PIC_POINTS)):
        a = NAME_PIC_POINTS[index]
        b = a[s]
        POST_POINTS.append(b)
        index = index + 1

L = 0
for i in USERNAMES:
    print "User " + str(i) + " has " + str(POST_POINTS[L]) + " points"
    L = L+1

MAX_VALUE = max(POST_POINTS)
MAX_INDEX = POST_POINTS.index(MAX_VALUE)


print "The winner is " + str(USERNAMES[MAX_INDEX])

