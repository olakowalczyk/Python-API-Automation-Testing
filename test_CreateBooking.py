import requests
import json
import jsonpath
from pyassert import *

URL = 'https://restful-booker.herokuapp.com/booking{}'


def get_booking(url, booking):
    return (requests.get(url.format(booking))).status_code


def delete_booking(url, booking):
    return (requests.delete(url.format(booking))).status_code


def test_create_booking():
    # Create booking
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
    response = requests.post(URL.format(''), data=data, headers=headers)

    # Tests
    response_json = json.loads(response.text)
    booking = jsonpath.jsonpath(response_json, '$.booking')[0]
    bookingid = jsonpath.jsonpath(response_json, '$.bookingid')[0]
    assert_that(response.status_code).is_equal_to(200)
    assert_that(booking).is_not_none()
    assert_that(bookingid).is_not_none()
    assert_that(get_booking(
        URL, ('/' + str(bookingid)))).is_equal_to(200)

    # Cleans up
    delete_booking(
        URL, ('/' + str(bookingid)))
