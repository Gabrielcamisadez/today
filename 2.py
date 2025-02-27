def get_all_devices(self, batch_size=100):
    start = 0
    all_devices = []

    while True:
        glpi_headers['Range'] = f"{start}-{start + batch_size - 1}"
        r1 = requests.get(self.domain, headers=glpi_headers, verify=False)
        
        if r1.status_code not in [200, 206]:  # 206 = Partial Content
            rich.print(f"Erro na requisição: {r1.status_code} - {r1.text}")
            break
        
        response = r1.json()

        if not isinstance(response, list) or len(response) == 0:
            break  # Se a resposta estiver vazia, termina a iteração

        for device in response:
            device.pop('links', None)
            all_devices.append(device.get('id'))
        
        start += batch_size  # Avança para a próxima página

    rich.print(f"Total de dispositivos obtidos: {len(all_devices)}")
    return all_devices

