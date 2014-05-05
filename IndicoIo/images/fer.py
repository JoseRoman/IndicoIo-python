import json

import requests
import numpy as np

base_url = "http://indico.io/api/fer/classify"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def fer(face):
    data_dict = json.dumps({"image": face})
    response = requests.post(base_url, data=data_dict, headers=headers)
    return response.content
