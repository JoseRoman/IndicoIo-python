import json

import requests
import numpy as np

from IndicoIo import JSON_HEADERS

base_url = lambda c: "http://api.indico.io/%s" % c

def facial_features(face):
    data_dict = json.dumps({"face": face})
    response = requests.post(base_url("facialfeatures"), data=data_dict, headers=JSON_HEADERS)
    response_dict = json.loads(response.content)
    return response_dict['response']
