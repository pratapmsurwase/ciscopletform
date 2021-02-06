from dnacentersdk import api
dnac = api.DNACenterAPI(
    username = "devnetuser",
    password = "Cisco123!",
    base_url = "https://sandboxdnac.cisco.com:443",
    version = '1.2.10',
    verify = False

)

devices = dnac.devices.get_device_list()
print(devices)
print('kkkkkkkk')
devices = dnac.devices.get_device_list()
devices = dnac.devices.get_device_list()