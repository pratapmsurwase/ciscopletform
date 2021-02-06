import requests
from credentails import sandbox1
print(sandbox1)
url = "{}/api/aaaLogin.json".format(sandbox1['URL'])
print(url)
r = requests.post(url, json={
    "aaaUser":{
        "attributes": {
            "name": LOGIN,
            "pwd" : PASSWORD
        }
    }
}, verify=False)
print(r.json())
token = r.json()['imdata'][0]["aaaLogin"]["attributes"]['token']
print(token)
tenant_url = '{}/api/node/class/fvTenant.json?query-target-filter=eq(fvTenant.name,"Heroes")'.format(URL)
QUERY_URL = URL + '/api/node/class/fvTenant.json?query-target-filter=eq(fvTenant.name,"Heroes")'
print(tenant_url)
cookie = {'APIC-cookie': token} 
tenant_re = requests.get(tenant_url, cookies=cookie, verify=False)
print(tenant_re.json()['imdata'][0]['fvTenant']['attributes']['dn'])