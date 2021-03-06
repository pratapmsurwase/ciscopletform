import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

username = 'developer'
password = 'BallGreenFoot23!'

url = 'https://devasc-nso-1.cisco.com/restconf/data/tailf-ncs:devices/device=junos0/config'
# url = 'https://devasc-nso-1.cisco.com/restconf/data/tailf-ncs:devices/device=ios0/config'
url_dev = 'https://devasc-nso-1.cisco.com/restconf/data/tailf-ncs:devices/'

headers = {'Content-Type': 'application/yang-data+json'}

#suprress credentials warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

response = requests.get( url, auth=(username, password),
                           headers=headers, verify=False)

print(response.text)