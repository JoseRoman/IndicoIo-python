import json

import requests
import numpy as np

from IndicoIo import JSON_HEADERS

base_url = lambda c: "http://indico.io/api/features/%s" % c

def facial(face):
    data_dict = json.dumps({"datums": face})
    response = requests.post(base_url("facial"), data=data_dict, headers=JSON_HEADERS)
    return json.loads(response.content)
