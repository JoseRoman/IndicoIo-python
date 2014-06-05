import requests
import json

from IndicoIo import JSON_HEADERS
from IndicoIo.utils import normalize

base_url = lambda c: "http://indico.io/api/%s" % c

def political(test_text):
    data_dict = json.dumps({'text': test_text})
    response = requests.post(base_url("political"), data=data_dict, headers=JSON_HEADERS)
    return json.loads(response.content)

def spam(test_text):
    data_dict = json.dumps({'text': test_text})
    response = requests.post(base_url("spam"), data=data_dict, headers=JSON_HEADERS)
    return json.loads(response.content)

def posneg(test_text):
    data_dict = json.dumps({'text': test_text})
    response = requests.post(base_url("sentiment"), data=data_dict, headers=JSON_HEADERS)
    return json.loads(response.content)
