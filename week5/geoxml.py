import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url =  "http://py4e-data.dr-chuck.net/comments_959744.xml"
print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)

results =  tree.findall('comments/comment')
print(len(results))
total=0
count=0
for i in results:
    temp=i.find('count').text
    # print(temp)
    count+=1
    total+=int(temp)
    # lat = results[0].find('comments').find('comment').find('count').text
    # location = results[0].find('formatted_address').text
print('sum:',total)
print('count:',count)
    # print('lat', lat, 'lng', lng)
    # print(location)