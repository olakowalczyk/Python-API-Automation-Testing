from pytest import fixture
from pyassert import *

from utils.http_manager import HttpManager
from api.bookings import Bookings


@fixture()
def response(test_data):
    data = test_data('test_data/create_booking.json')
    response = HttpManager.post(Bookings.CREATE_BOOKING, data)
    yield response
    HttpManager.delete(Bookings.DELETE_BOOKING.format(response.json()['bookingid']))


class PostTests:

    def test_create_booking(self, response):
        """
        Checks whether new booking is properly created
        """
        assert_that(response.status_code).is_equal_to(200)
        assert_that((HttpManager.get(Bookings.GET_BOOKING.format(response.json()['bookingid']))).status_code).is_equal_to(200)
