import requests
import json

base_url = lambda c: "http://localhost/api/sentiment/%s/classify" % c
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def political(test_text):
    data_dict = json.dumps({'text': test_text})
    response = requests.post(base_url("political"), data=data_dict, headers=headers)
    return json.loads(response.content)

def spam(test_text):
    data_dict = json.dumps({'text': test_text})
    response = requests.post(base_url("spam"), data=data_dict, headers=headers)
    return json.loads(response.content)

def sentiment(test_text):
    data_dict = json.dumps({'text': test_text})
    response = requests.post(base_url("sentiment"), data=data_dict, headers=headers)
    return json.loads(response.content)

print political("Guns don't kill people, people kill people.")
print spam("Get a Free Car!!")
print sentiment("Worst Car Ever.")
