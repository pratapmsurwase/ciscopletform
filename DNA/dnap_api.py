import requests 
from requests.auth import HTTPBasicAuth
from credentails import *


def dnaToken(username, password, url):
    url_dna = "{}/dna/system/api/v1/auth/token".format(url) 
    print(url_dna)
    # username="devnetuser"
    # password="Cisco123!"

    headers = {'content-type': 'application/json'}     

    token_response = requests.post(url_dna, auth=(username, password), headers=headers, verify=False)
    data = token_response.json()
    return data['Token']

def device_detail(url, token):
    url_device = "{}/dna/intent/api/v1/network-device".format(url) 
    headers = { 'content-type': 'application/json', 'x-auth-token' : token}
    response  = requests.get(url_device, headers=headers)
    print(response)
    return response.json()["response"] 

if __name__ == '__main__':
    token_url = dnaToken(username, password, url)
    device_data  = device_detail(url, token_url)
    print(token_url)
    for device in device_data:
        print( 'The Hostname is {} , and Family Name {}'.format(device['hostname'], device['family']))
        print('The IP-Add is {}, Version is {}'.format(device['managementIpAddress'], device['softwareVersion']))
