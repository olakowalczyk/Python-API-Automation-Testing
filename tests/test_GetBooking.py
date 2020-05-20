import requests
from pyassert import *
from common.bookings import Bookings

URL = 'https://restful-booker.herokuapp.com/booking/{}'
BOOKING = Bookings.get_random_booking()


def test_get_booking():
    '''Checks whether booking with given id is returned'''
    # GET Request: Gets booking
    response = requests.get(URL.format(BOOKING))
    # Tests
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()['firstname']).is_instance_of(str)
    assert_that(response.json()['depositpaid']).is_instance_of(bool)
