
import meraki
import pprint

api_key =  '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
url = 'https://dashboard.meraki.com'
org_name = 'Meraki Live Sandbox'

dashboard = meraki.DashboardAPI(
      api_key = api_key,
      base_url = url + '/api/v0',
      output_log = False,
      print_console = False
)

org_list = dashboard.organizations.getOrganization()
for org in org_list:
    if org['name'] == org_name:
        my_org = org['id']

inventory_list = dashboard.organizations.getOrganization(my_org)
pprint(inventory_list)