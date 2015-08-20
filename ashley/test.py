#!/usr/bin/python
import requests
import cgi
import json

print "Content-type: text/html\n";
data = cgi.FieldStorage();
email = data['email'].value;
payload = {'email':email};
r = requests.post("https://ashley.cynic.al/check", data=payload,timeout=100);
json_val = r.json();

if not json_val['success']:
	ret = 'Error'
else:
	ret = str(json_val['found'])
print '{"found":"' + ret + '"}'