import requests
from pyassert import *

from utils.http_manager import HttpManager
from common.bookings import Bookings


def test_get_booking():
    """
    Checks whether booking with given id is returned
    """
    response = HttpManager.get(f'{Bookings.BASE_URL}/booking/' + str(Bookings.get_random_booking()))
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()['firstname']).is_instance_of(str)
    assert_that(response.json()['depositpaid']).is_instance_of(bool)
