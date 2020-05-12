import requests
import jsonpath
import json
from pyassert import *

URL = 'https://restful-booker.herokuapp.com/booking'


def test_get_booking_ids():
    # Gets booking ids
    response = requests.get(URL)

    # Tests
    response_json = json.loads(response.text)
    bookingid = jsonpath.jsonpath(response_json, '$[0].bookingid')[0]
    assert_that(response.status_code).is_equal_to(200)
    assert_that(bookingid).is_instance_of(int)
