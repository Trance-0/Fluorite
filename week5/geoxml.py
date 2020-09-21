import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url =  "http://py4e-data.dr-chuck.net/comments_959744.xml"
print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

results =  tree.findall('comments/comment')
print(len(results))
total=0
count=0
for i in results:
    temp=i.find('count').text
    count+=1
    total+=int(temp)
print('sum:',total)
print('count:',count)