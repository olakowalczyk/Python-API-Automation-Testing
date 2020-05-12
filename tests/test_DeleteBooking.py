import requests
import json
import jsonpath
import random
import pytest
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


def get_booking(url, booking):
    return (requests.get(url.format(booking))).status_code


# Expected to fail because DELETE returns '201 Created' response instead of '200 OK'
if get_booking(URL, BOOKING) == 200:  # Pre-check: GET booking
    @pytest.mark.xfail()
    def test_delete_booking(token):

        # Delete booking
        headers = {'Cookie': 'token=' + str(token)}
        response = requests.delete(URL.format(BOOKING), headers=headers)

        # Tests
        assert_that(response.status_code).is_equal_to(200)
        assert_that(get_booking(URL, BOOKING)).is_equal_to(404)

else:
    raise Exception('GET pre-request failed')
