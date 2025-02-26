NETBOX_URL = "https://srvnetboxdsv-trf1.trf1.gov.br/api/dcim/devices"
NETBOX_TOKEN = "b6d1d226d2ef35b4bf1dd0cdc98a1851d16d4475"

GLPI_URL = "http://localhost:9090/apirest.php/Computer/"
GLPI_TOKEN = "nj5iOfzdC74IwSs8c1i4BZdj02ABi6DKVQH3Ep8y"
GLPI_SESSION_TOKEN = "b191f946afe3e49aed3fbaa2f309e672"

GLPI_HEADERS = {
            "Content-Type": "application/json",
            "Authorization": "Basic Z2xwaTpnbHBp",
            "Session-Token": GLPI_SESSION_TOKEN,
            "App-Token": GLPI_TOKEN,
        }

NETBOX_HEADERS = {
            "Authorization": f"Token {NETBOX_TOKEN}",
            "Content-Type": "application/json",
        }