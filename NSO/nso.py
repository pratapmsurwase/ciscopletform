import requests
import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning

base_url = 'https://devasc-nso-1.cisco.com'
username = 'developer'
password = 'BallGreenFoot23!'
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

get_device_url = base_url + '/restconf/data/tailf-ncs:devices/device'

headers = {
    'Content-Type': 'application/yang-data+json'
}

response = requests.get(get_device_url, auth=(username, password), 
                               headers=headers,
                               verify= False) 
print(response.text)
##pprint.pprint(response.text)