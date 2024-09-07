import requests

YANDEX_DISK_API_URL = "https://cloud-api.yandex.net:443/v1/disk/resources"
YANDEX_DISK_TOKEN = ""

def create_folder(folder_path):
    headers = {
        'Authorization': f'OAuth {YANDEX_DISK_TOKEN}'
    }
    params = {
        'path': folder_path
    }
    response = requests.put(f'{YANDEX_DISK_API_URL}/mkdir', headers=headers, params=params)
    return response
