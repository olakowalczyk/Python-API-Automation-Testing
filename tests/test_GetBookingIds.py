import requests
from pyassert import *

from common.bookings import Bookings

URL = f'{Bookings.BASE_URL}/booking'


def test_get_booking_ids():
    '''Checks whether bookings are returned'''
    # GET Request: Gets booking ids
    response = requests.get(URL)
    response_json = response.json()
    # Tests
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response_json[0]['bookingid']).is_instance_of(int)
