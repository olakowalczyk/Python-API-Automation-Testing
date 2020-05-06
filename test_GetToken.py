import requests
import json
import jsonpath
from pyassert import *


def test_get_auth_token():
    url_auth = 'https://restful-booker.herokuapp.com/auth'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({
        'username': 'admin',
        'password': 'password123'
    })
    response = requests.post(url_auth, data=data, headers=headers)
    assert_that(response.status_code).is_equal_to(200)
    response_json = json.loads(response.text)
    token = jsonpath.jsonpath(response_json, 'token')
    assert_that(token[0]).is_not_none()
    assert_that(token[0]).is_instance_of(str)

    return token
