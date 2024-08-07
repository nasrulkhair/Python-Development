
#opening files in browser using url library
import urllib.request, urllib.parse, urllib.error

web = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
print(web)
for line in web:
    print(line.decode().strip())
    

# Web scraping using Beautiful soup
 
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
 
url = input("Enter link: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("a")
for tag in tags:
    print(tag.get("href", None)) 
    
#XML Element Tree

import xml.etree.ElementTree as ET
input = '''
<stuff>
    <users>
        <user x ="2">
            <id>001</id>
            <name>Nasrul</name>
        </user>
        <user x ="7">
            <id>002</id>
            <name>Khair</name>
        </user>
    </users>
</stuff> 
'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count: ', len(lst))
for item in lst:
    print('Name: ', item.find('name').text)
    print('Id: ', item.find("id").text)
    print('Attribute: ', item.get('x'))
    
# Javascript Object Notation (JSON)

import json
data = '''{
    "name": "Chuck",
    "phone": {
        "type": "intl",
        "number": "+1 734 303 4456"
    },
    "email": {
        "hide": "yes"
    }

}'''

info = json.loads(data)
print("Name: ", info["name"])
print("Hide: ", info["email"]["hide"])