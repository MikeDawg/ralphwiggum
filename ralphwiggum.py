#!/usr/bin/python

import requests
import json
import re
import math
import datetime

mydate=datetime.datetime.now()

# First find out how many hits there are
r=requests.get("https://www.googleapis.com/customsearch/v1?key=GOOGLE_API_KEY&cx=GOOGLE_APP_ID&q=QUERY&alt=json")
myjson=json.loads(r.text)
print "Total number of hits: "+myjson["searchInformation"]["totalResults"]

numhits=myjson["searchInformation"]["totalResults"]
if numhits > 10:
	iterator=int(math.ceil((float(numhits))/10))
	for i in range(iterator):
		startnum=str(str(i)+str(1))
		r=requests.get("https://www.googleapis.com/customsearch/v1?key=GOOGLE_API_KEY&cx=GOOGLE_APP_ID&q=QUERY&alt=json&start="+startnum)
		myjson=json.loads(r.text)
		for hit in myjson["items"]:
			date=re.match('\w+ \d+\, \d+',hit["snippet"])
			if date:
                		print str(date.group())+" "+hit["formattedUrl"]
			else:
				print mydate.strftime("%b %d, %Y")+" "+hit["formattedUrl"]
else:
	for hit in myjson["items"]:
	        date=re.match('\w+ \d+\, \d+',hit["snippet"])
	        print str(date.group())+" "+hit["formattedUrl"]
