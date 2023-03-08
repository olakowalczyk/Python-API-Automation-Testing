import json
import pytest
import requests

from common.bookings import Bookings

@pytest.fixture()
def token():
    '''Returns token which will be used (as a fixture) in the test fucntions that require authentication'''
    URL_AUTH = f'{Bookings.URL}/auth'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({
        'username': 'admin',
        'password': 'password123'
    })
    response = requests.post(URL_AUTH, data=data, headers=headers)
    response_json = json.loads(response.text)
    return response_json['token']
