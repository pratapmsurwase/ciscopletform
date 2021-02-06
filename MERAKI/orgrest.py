import requests
import pprint

def get_org_id(url, headers, name):
    org_list = requests.get(url + '/api/v0/organizations', headers=headers).json()
    for org in org_list:
        if org['name'] == name:
            return org['id']


def get_inventory(url, headers, org_id):
    inventory_list = requests.get(url + '/api/v0/organizations/' +  org_id  + '/inventory',
                              headers=headers).json()
    return inventory_list    

myheaders = {'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'}
url = 'https://dashboard.meraki.com'
org_name = 'Meraki Live Sandbox'
org_id = get_org_id(url, myheaders, org_name) 
inventory_list = get_inventory(url, myheaders, org_id)
print(org_id)
pprint(inventory_list)