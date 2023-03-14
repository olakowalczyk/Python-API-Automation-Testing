import json
from pyassert import *

from utils.http_manager import HttpManager
from common.bookings import Bookings


def test_create_booking():
    """
    Checks whether new booking is properly created
    """
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
    response = HttpManager.post(f'{Bookings.BASE_URL}/booking', data)

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()['bookingid']).is_not_none()
    assert_that(response.json()['booking']).is_not_none()
    assert_that((HttpManager.get(f'{Bookings.BASE_URL}/booking'.format(
        '/' + str(response.json()['bookingid'])))).status_code).is_equal_to(200)
    # Cleans up
    HttpManager.delete(f'{Bookings.BASE_URL}'.format('/' + str(response.json()['bookingid'])))
