#Web Services

{
    "status": "OK",
    "results": [
        {
            "geometry": {
                "location_type": "APPROXIMATE",
                "location": {
                    "lat": 42.2808256,
                    "long": -83.7430378
                }
            },
            "address_components": [
                {
                    "long_name": "Ann Arbor",
                    "types": [
                        "locality",
                        "political"
                    ],
                    "short_name": "Ann Arbor"
                }
            ],
            "formatted_address": "Ann Arbor, MI, USA",
            "types": [
                "locality",
                "political"
            ]
        }
    ]
}


# Code untuk dapatkan lattitude and longitude based on location provided.
# Syaratnya kena dapatkan permission or request to use the API from Google platform first. Cannot simply use
#Make sure tak suka2 published dekat public repository or any public location


import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?key=YOUR_API_KEY&'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    
    url = serviceurl + urllib.parse.urlencode({'address': address})
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    
    try:
        js = json.loads(data)
    except:
        js = None
        
    if not js or 'status' not in js or js['status'] != 'OK':
        print('===== Failure to Retrieve ====')
        print(data)
        continue
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    
    print('lat: ', lat, 'lng: ', lng)
    location = js['results'][0]['formatted_address']
    print(location)


# Corrected version

import urllib.request, urllib.parse, urllib.error
import json

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?key=YOUR_API_KEY&'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    
    # Fix the typo from 'urlib' to 'urllib'
    url = serviceurl + urllib.parse.urlencode({'address': address})
    
    print('Retrieving', url)
    # Fix the typo from 'urlib' to 'urllib'
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    
    try:
        js = json.loads(data)
    except:
        js = None
        
    if not js or 'status' not in js or js['status'] != 'OK':
        print('===== Failure to Retrieve ====')
        print(data)
        continue
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]  # Changed 'long' to 'lng' to avoid conflict with Python keyword
    
    print('lat:', lat, 'lng:', lng)
    location = js['results'][0]['formatted_address']
    print(location)

