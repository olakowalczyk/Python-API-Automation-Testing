import requests
import json
import jsonpath
from pyassert import *


def test_get_booking():
    url_booking = 'https://restful-booker.herokuapp.com/booking/{}'

    response = requests.get(url_booking.format(1))
    assert_that(response.status_code).is_equal_to(200)

    json_response = json.loads(response.text)
    firstname = jsonpath.jsonpath(json_response, 'firstname')
    assert_that(firstname[0]).is_instance_of(str)
    depositpaid = jsonpath.jsonpath(json_response, 'depositpaid')
    assert_that(depositpaid[0]).is_instance_of(bool)
