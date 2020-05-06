import requests
import jsonpath
import json
from pyassert import *


def test_get_booking_ids():
    url = 'https://restful-booker.herokuapp.com/booking'
    response = requests.get(url)

    assert_that(response.status_code).is_equal_to(200)

    response_json = json.loads(response.text)
    bookingid = jsonpath.jsonpath(response_json, '$[0].bookingid')

    assert_that(bookingid[0]).is_instance_of(int)
