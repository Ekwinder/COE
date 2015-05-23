import urllib2
import json

def fullContactCollect(email):
	api_key = '46edc4c0fddc20d7'
	email = email
	fullURL = 'https://api.fullcontact.com/v2/person.json?apiKey='+api_key+'&email=' + email
	loadurl = urllib2.urlopen(fullURL)
	jsondata = json.load(loadurl)
	print jsondata
	photos  = jsondata['photos']

	for item in photos:
		print item['url']

fullContactCollect('markcuban@dallasmavs.com')