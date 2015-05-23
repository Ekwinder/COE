import urllib2
import json

locu_api = 'e785290ab5496140b5c73c73d0f0dbee660c8507'

def locu_search(query):
	api_key = locu_api
	url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
	locality = query.replace(' ','%20')
	final_url = url + "&locality="+locality +"&category=restaurant"
	json_obj = urllib2.urlopen(final_url)
	data = json.load(json_obj)

	for item in data['objects']:
		print item['name'], item['phone']

locu_search('New York ')