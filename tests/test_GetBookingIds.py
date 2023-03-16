from pyassert import *

from utils.http_manager import HttpManager
from common.bookings import Bookings


def test_get_booking_ids():
    """
    Checks whether bookings are returned
    """
    response = HttpManager.get(Bookings.GET_BOOKINGS)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()[0]['bookingid']).is_instance_of(int)
