import json
import requests
from pyassert import *

URL = 'https://restful-booker.herokuapp.com/booking{}'


def test_create_booking():
    '''Checks whether new booking is properly created'''
    # POST Request: Creates booking
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
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()['bookingid']).is_not_none()
    assert_that(response.json()['booking']).is_not_none()
    assert_that((requests.get(URL.format(
        '/' + str(response.json()['bookingid'])))).status_code).is_equal_to(200)
    # Cleans up
    requests.delete(URL.format('/' + str(response.json()['bookingid'])))
