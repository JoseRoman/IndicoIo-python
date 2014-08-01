import requests
import json

from indicoio import JSON_HEADERS

base_url = lambda c: "http://api.indico.io/%s" % c

def language(test_text):
    data_dict = json.dumps({'text': test_text})
    response = requests.post(base_url("language"), data=data_dict, headers=JSON_HEADERS)
    return json.loads(response.content)
