import requests
import json
import jsonpath
from pyassert import *
import test_GetToken


def test_update_booking():
    token = test_GetToken.test_get_auth_token()

    url = 'https://restful-booker.herokuapp.com/booking/{}'
    headers = {'Content-Type': 'application/json',
               'Cookie': 'token=' + str(token[0])}
    data = json.dumps({
        "firstname": "Edited",
        "lastname": "Edited"
    })
    response = requests.patch(url.format(2), data=data, headers=headers)
    response_json = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    firstname = jsonpath.jsonpath(response_json, 'firstname')
    lastname = jsonpath.jsonpath(response_json, 'lastname')
    assert_that(firstname[0]).is_equal_to('Edited')
    assert_that(lastname[0]).is_equal_to('Edited')
