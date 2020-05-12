import requests
import json
import jsonpath
import random
from pyassert import *

URL = 'https://restful-booker.herokuapp.com/booking/{}'
BOOKING = random.randrange(1, 10, 1)


def test_get_booking():
    # Gets booking
    response = requests.get(URL.format(BOOKING))

    # Tests
    response_json = json.loads(response.text)
    firstname = jsonpath.jsonpath(response_json, 'firstname')
    depositpaid = jsonpath.jsonpath(response_json, 'depositpaid')
    assert_that(response.status_code).is_equal_to(200)
    assert_that(firstname[0]).is_instance_of(str)
    assert_that(depositpaid[0]).is_instance_of(bool)
