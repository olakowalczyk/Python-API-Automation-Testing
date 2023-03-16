from pyassert import *

from utils.http_manager import HttpManager
from common.bookings import Bookings


class TestGet:

    def test_get_booking(self):
        """
        Checks whether booking with given id is returned
        """
        response = HttpManager.get(Bookings.GET_BOOKING.format(Bookings.get_random_booking()))
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()['firstname']).is_instance_of(str)
        assert_that(response.json()['depositpaid']).is_instance_of(bool)


    def test_get_booking_ids(self):
        """
        Checks whether bookings are returned
        """
        response = HttpManager.get(Bookings.GET_BOOKINGS)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()[0]['bookingid']).is_instance_of(int)
        