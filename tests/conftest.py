import json
import pytest
import requests


@pytest.fixture()
def token():
    '''Returns token which will be used (as a fixture) in the test fucntions that require authentication'''
    URL_AUTH = 'https://restful-booker.herokuapp.com/auth'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({
        'username': 'admin',
        'password': 'password123'
    })
    response = requests.post(URL_AUTH, data=data, headers=headers)
    response_json = json.loads(response.text)
    return response_json['token']
