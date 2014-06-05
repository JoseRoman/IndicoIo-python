import json

import requests
import numpy as np
from IndicoIo import JSON_HEADERS

base_url = "http://indico.io/api/fer"

def fer(face):
    data_dict = json.dumps({"face": face})
    response = requests.post(base_url, data=data_dict, headers=JSON_HEADERS)
    return json.loads(response.content)
