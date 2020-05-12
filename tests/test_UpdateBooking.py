import requests
import json
import jsonpath
import random
from pyassert import *


URL = 'https://restful-booker.herokuapp.com/booking/{}'

# Provides the list of currently existing bookings
def existing_bookings():
    url = 'https://restful-booker.herokuapp.com/booking'
    response = (requests.get(url)).json()
    for booking in response:
        bookingids = jsonpath.jsonpath(response, '$.[bookingid]')
    return list(bookingids)


BOOKING = random.choice(existing_bookings())
UPDATE = 'Edited'

# GET Pre-request: Takes booking and its firstname
get_response = requests.get(URL.format(BOOKING))
get_firstname = jsonpath.jsonpath(get_response.json(), '$.firstname')[0]


def test_update_booking(token):
    # PUT: Updates booking
    headers = {'Content-Type': 'application/json',
               'Cookie': 'token=' + str(token)}
    put_data = json.dumps({
        "firstname": "{}".format(UPDATE),
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    })
    put_response = requests.put(URL.format(
        BOOKING), data=put_data, headers=headers)

    # Tests
    put_firstname = jsonpath.jsonpath(put_response.json(), '$.firstname')[0]
    put_data_json = json.loads(put_data)
    assert_that(put_response.status_code).is_equal_to(200)
    assert_that(put_firstname).is_not_equal_to(get_firstname)
    assert_that(put_firstname).is_equal_to(
        jsonpath.jsonpath(put_data_json, '$.firstname')[0])

    # Cleans up
    cleaning_up_data = json.dumps({
        "firstname": "{}".format(get_firstname),
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    })
    requests.put(URL.format(
        BOOKING), data=cleaning_up_data, headers=headers)
