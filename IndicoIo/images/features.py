import json

import requests
import numpy as np

from IndicoIo import JSON_HEADERS

base_url = lambda c: "http://indico.io/api/features/%s" % c

def facial_features(face, full_return=False):
    data_dict = json.dumps({"datums": face})
    response = requests.post(base_url("facial"), data=data_dict, headers=JSON_HEADERS)
    response_dict = json.loads(response.content)
    if full_return:
        return response_dict
    return json.loads(response_dict['feature_vector'])
