import json

import requests
import numpy as np

base_url = lambda c: "http://indico.io/api/features/%s" % c
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def facial(face):
    data_dict = json.dumps({"datums": face})
    response = requests.post(base_url("facial"), data=data_dict, headers=headers)
    return response.content
