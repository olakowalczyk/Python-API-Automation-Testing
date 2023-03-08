import requests
import json
from pyassert import *
from common.bookings import Bookings

URL = f'{Bookings.URL}/booking/'
BOOKING = Bookings.get_random_booking()
UPDATE = 'Edited'


# GET Pre-request: Takes booking and its firstname
get_response = requests.get(URL+str(BOOKING))
get_firstname = get_response.json()['firstname']


def test_update_booking(token):
    '''Checks whether update properly updates booking data'''
    # PUT request: Updates booking
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
    put_response = requests.put(URL+str(BOOKING), data=put_data, headers=headers)
    put_firstname = put_response.json()['firstname']
    put_data_json = json.loads(put_data)
    # Tests
    assert_that(put_response.status_code).is_equal_to(200)
    assert_that(put_firstname).is_not_equal_to(get_firstname)
    assert_that(put_firstname).is_equal_to(put_data_json['firstname'])
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
