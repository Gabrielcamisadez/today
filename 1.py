import json
import urllib3
import requests
import rich
from config import NETBOX_URL, GLPI_URL

urllib3.disable_warnings()


# ========================================================================
#                             Netbox
# ========================================================================

NETBOX_TOKEN = "b6d1d226d2ef35b4bf1dd0cdc98a1851d16d4475"

netbox_headers = {
    "Authorization": f"Token {NETBOX_TOKEN}",
    "Content-Type": "application/json"
}
   
class Netbox():
    def __init__(self):
        self.domain = "http://localhost:8000/api/dcim/devices"
        self.ip = "127.0.0.1"

    def get_device(self):           
        r1 = requests.get(self.domain, headers=netbox_headers, verify=False)
        response = r1.json()

        if isinstance(response, dict):
            rich.print(json.dumps(response, indent=4))

        if isinstance(response, list):
            rich.print(json.dumps(response, indent=4))

    
    def get_device_name(self):
        r1 = requests.get(self.domain, headers=netbox_headers, verify=False)
        response = r1.json()

        for device in response['results']:
            rich.print(json.dumps(device['name'], indent=4))

    
    def get_device_role_name(self):
        r1 = requests.get(self.domain, headers=netbox_headers, verify=False)
        response = r1.json()

        for device in response['results']:
            rich.print(f"\t\n{device['role']['name']}")
            rich.print(f"{device['role']['id']}")

    
    def get_device_site(self):
        r1 = requests.get(self.domain, headers=netbox_headers, verify=False)
        response = r1.json()

        for device in response['results']:
            rich.print(f"\t\n{device['site']['name']}")
            rich.print(f"{device['site']['id']}")



# ========================================================================
#                             Glpi
# ========================================================================

GLPI_TOKEN = "nj5iOfzdC74IwSs8c1i4BZdj02ABi6DKVQH3Ep8y"

glpi_headers = {
    "Authorization": "Basic Z2xwaTpnbHBp",
    "Content-Type": "application/json",
    "App-Token": GLPI_TOKEN,
    "Session-Token": "8f32144f76e71b0ca378c2dd42501855",
    "Range": "0-9"   
}

class Glpi():
    def __init__(self):
        self.domain = "http://localhost:9090/apirest.php/Computer"
        self.ip = "127.0.0.1"

    def get_session_token(self):
        r1 = requests.get(self.domain, headers=glpi_headers, verify=False)
        print(r1.text)


    def get_device(self):
        r1 = requests.get(self.domain, headers=glpi_headers, verify=False)
        response = r1.json()

        if isinstance(response, dict):
            rich.print(json.dumps(response, indent=4))

        if isinstance(response, list):
            for device in response:
                device.pop('links')
                rich.print(device)

    def get_all_devices(self):
        r1 = requests.get(self.domain, headers=glpi_headers, verify=False)
        response = r1.json()

        for device in response:
            device.pop('links')
            rich.print(device.get('id'))

    def map_infos(self):
        r1 = requests.get(self.domain, headers=glpi_headers, verify=False)
        response = r1.json()
        netbox_data = [{

        }]

        for device in response [:3]:
            device.pop('links')
            netbox_data.append({
                "id": device.get('id'),
                "name": device.get('name'),
                "device_type": device.get('computertypes_id'),
                "site": device.get('locations_id'),
                "role": device.get('computertypes_id')
            })

            rich.print(netbox_data)





            
    def get_computer_type(self):
        r1 = requests.get(self.domain, headers=glpi_headers, verify=False)
        response = r1.json()

        for device in response:
            device.pop('links')
            if device['computertypes_id'] in self.computertype_map:
                rich.print(f"\t{device['computertypes_id']}")
                rich.print(f"\t{self.computertype_map[device['computertypes_id']]}")



g = Glpi()
# g.get_device()
g.map_infos()
# g.get_all_devices()
# g.get_session_token()
# g.get_computer_type()
# ========================================================================
n = Netbox()
# n.get_device()
# n.get_device_name()
# n.get_device_role_name()
# n.get_device_site()
