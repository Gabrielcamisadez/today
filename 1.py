from config import NETBOX_TOKEN, NETBOX_URL, NETBOX_HEADERS, GLPI_TOKEN, GLPI_URL, GLPI_SESSION_TOKEN, GLPI_HEADERS
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




# ======================================================================
# --- NETBOX   
# ======================================================================

class Netbox():
    def __init__(self):
        self.domain = "https://srvnetboxdsv-trf1.trf1.gov.br/api/dcim/devices"
        self.token = NETBOX_TOKEN
        self.headers = {
            "Authorization": f"Token {self.token}",
            "Content-Type": "application/json",
        }
            
       

    def get_device(self):
        import requests
        r1 = requests.get(self.domain, headers=self.headers, verify=False)
        
        try:
            response = r1.json()
        except:
            print("format", r1.text)
            return

        if isinstance(response, dict) and "data" in response:
            response = response["data"]
        elif not isinstance(response, list):
            print("Error", response)
            return    
            
        for device in response:
            if isinstance(device, dict):
                device.pop("links", None)    
        return response            


# ======================================================================
# --- GLPI
# ======================================================================

class GLPI():
    def __init__(self):
        self.domain = GLPI_URL
        self.headers = {
            "App-Token": GLPI_TOKEN,
            "Content-Type": "application/json",
            "Session-Token": GLPI_SESSION_TOKEN,
            "Authorization": "Basic Z2xwaTpnbHBp"
        }
        

    def get_init_session_token(self):
        import requests
        init_url = "http://localhost:9090/apirest.php/initSession"
        r1 = requests.get(init_url, headers=self.headers, verify=False)
        print(r1.text)


    def get_device(self):
        import requests
        r1 = requests.get(self.domain, headers=self.headers, verify=False)
        response = r1.json()
        
        if isinstance(response, dict):
            response.pop("links", None)
            print(json.dumps(response, indent=4))
            return
        
        if isinstance(response, list):
            for device in response:
                device.pop("links", None)
                print(json.dumps(device, indent=4))

        return response


    def get_device_name(self):
        import requests
        r1 = requests.get(self.domain, headers=self.headers, verify=False)
        response = r1.json()
        
        if isinstance(response, dict):
            print(response["name"])
            return
        
        if isinstance(response, list):
            for device in response:
                print(device.get("name"))
        
     
    def get_device_type(self):
        import requests
        r1 = requests.get(self.domain, headers=self.headers, verify=False)
        try :
            response = r1.json()
        except:
            print("format", r1.text)
            return
        
        if isinstance(response, dict):
            print(response.get("computertypes_id"))
            return
      
        if isinstance(response, list):
            for device in response:
                print(device.get("computertypes_id"))

    
    def get_device_location(self):
        import requests
        r1 = requests.get(self.domain, headers=self.headers, verify=False)
        try:
            response = r1.json()
        except:
            print("format", r1.text)
            return
        
        if isinstance(response, dict):
            print(response.get("locations_id"))
            return
        
        if isinstance(response, list):
            for device in response:
                print(device.get("locations_id"))

# ================================

    def data_to_netbox(self):
        import requests
        to_netbox = []
        r1 = requests.get(self.domain, headers=self.headers, verify=False)
        response = r1.json()

        if isinstance(response, dict):
            response = [response]

        if isinstance(response, list):
            for device in response:
                device.pop("links", None)
                device.pop("id", None)
                device.pop("contact_num", None)
                device.pop("entities_id", None)
                device.pop("otherserial", None)
                device.pop("is_deleted", None)
                device.pop("ticket_tco", None)
                device.pop("is_recursive", None)
                device.pop("states_id", None)
                device.pop("users_id", None)
                device.pop("users_id_tech", None)
                device.pop("autoupdatesystems_id", None)
                device.pop("is_dynamic", None)
                device.pop("last_boot", None)
                device.pop("template_name", None)
                device.pop("is_template", None)
                device.pop("last_inventory_update", None)
                device.pop("groups_id_tech", None)
                device.pop("networks_id", None)
                to_netbox.append(device)

        print(json.dumps(to_netbox, indent=4))
        return to_netbox
    
    
    def send_to_netbox(self):
        import requests
        to_netbox = self.data_to_netbox()
        for device in to_netbox:
            r1 = requests.post(NETBOX_URL, headers=NETBOX_HEADERS, data=json.dumps(device), verify=False)
            print(r1.status_code)
            print(r1.headers)
            print(r1.request.headers)
            print(r1.request.body)
            print("====================================")
            print("====================================")
        
        


n = Netbox()
# n.get_device()

# ================================

g = GLPI()
# g.get_device()
# g.get_device_location()
# g.get_device_name()
# g.get_device_type()
# g.data_to_netbox()
g.send_to_netbox()