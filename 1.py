import json
import urllib3
import requests
import rich

urllib3.disable_warnings()


# ========================================================================
#                             Netbox
# ========================================================================

NETBOX_TOKEN = "1ec53d4afb6b10cd085586b44b37e985760140ce"

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

GLPI_TOKEN = "ltUAk7vrdlavcCoXWBAHze6rIeTexMblGuUevUMO"

glpi_headers = {
    "Authorization": "Basic Z2xwaTpnbHBp",
    "Content-Type": "application/json",
    "App-Token": GLPI_TOKEN,
    "Session-Token": "670d8eb03a46b78c82aaf26005df88ce"
}

class Glpi():
    def __init__(self):
        self.domain = "http://localhost:8080/apirest.php/Computer"
        self.ip = "127.0.0.1"

    def get_session_token(self):
        r1 = requests.get(self.domain, headers=glpi_headers, verify=False)
        print(r1.text)


    def get_device(self):
        r1 = requests.get(self.domain, headers=glpi_headers, verify=False)
        response = r1.json()

        for device in response:
            device.pop('links')
            rich.print(device)


    computertype_map = {
        0: "Desktop",
        1: "Server",
        2: "VM"
    }            

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
g.get_computer_type()
# ========================================================================
n = Netbox()
# n.get_device()
# n.get_device_name()
# n.get_device_role_name()
# n.get_device_site()
