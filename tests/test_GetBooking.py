import requests
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


def test_get_booking():
    # Gets booking
    response = requests.get(URL.format(BOOKING))

    # Tests
    firstname = jsonpath.jsonpath(response.json(), '$.firstname')[0]
    depositpaid = jsonpath.jsonpath(response.json(), '$.depositpaid')[0]
    assert_that(response.status_code).is_equal_to(200)
    assert_that(firstname).is_instance_of(str)
    assert_that(depositpaid).is_instance_of(bool)
