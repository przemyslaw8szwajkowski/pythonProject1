import xml.etree.ElementTree as ET
import requests
import json

import response as response
import xmltodict

# r = requests.get("https://api.nbp.pl/api/exchangerates/rates/c/EUR/today/")
# print(r.content)
#
# requestURL = 'https://api.nbp.pl/api/exchangerates/rates/c/EUR/today/'
# # tree = ET.fromstring(response.content)
# # root = tree.getroot()
# # root = ET.fromstring(r.content)
# root = ET.parse(urllib2.urlopen(requestURL)).getroot()
# print(root)
response = requests.get("https://api.nbp.pl/api/exchangerates/rates/c/EUR/today/?format=json",params = parameters)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())


print(response.content)