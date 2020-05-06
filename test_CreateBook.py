import requests
import json
import jsonpath
from pyassert import *


def test_create_book():
    url = 'https://restful-booker.herokuapp.com/booking'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    })
    response = requests.post(url, data=data, headers=headers)
    assert_that(response.status_code).is_equal_to(200)
    response_json = json.loads(response.text)
    bookingid = jsonpath.jsonpath(response_json, '$.bookingid')
    assert_that(bookingid[0]).is_not_none()
    booking = jsonpath.jsonpath(response_json, '$.booking')
    assert_that(booking[0]).is_not_none()
