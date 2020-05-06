import requests
import json
import jsonpath
from pyassert import *
import test_GetToken


def test_delete_booking():
    token = test_GetToken.test_get_auth_token()

    url = 'https://restful-booker.herokuapp.com/booking/{}'
    headers = {'Cookie': 'token=' + str(token[0])}
    response = requests.delete(url.format(3), headers=headers)
    assert_that(response.status_code).is_equal_to(201)
