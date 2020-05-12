import requests
import json
import jsonpath
import pytest


@pytest.fixture()
def token():
    URL_AUTH = 'https://restful-booker.herokuapp.com/auth'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({
        'username': 'admin',
        'password': 'password123'
    })
    response = requests.post(URL_AUTH, data=data, headers=headers)
    response_json = json.loads(response.text)
    return (jsonpath.jsonpath(response_json, 'token'))[0]
