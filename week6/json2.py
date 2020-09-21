import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url =  "http://py4e-data.dr-chuck.net/comments_959745.json"
print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read()

info = json.loads(data)
print('User count:', len(info))

comments=info['comments']
sumofcount=0
sumofuser=0

for i in comments:
    sumofcount+=int(i['count'])
    sumofuser+=1

print('count',sumofuser)
print('sum:',sumofcount)