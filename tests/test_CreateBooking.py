from pytest import fixture
from pyassert import *

from utils.http_manager import HttpManager
from api.bookings import Bookings


@fixture()
def test_data() -> str:
    with open('test_data/create_booking.json') as data_file:
        data = data_file.read()
        return data


@fixture()
def response(test_data):
    response = HttpManager.post(Bookings.CREATE_BOOKING, test_data)
    yield response
    HttpManager.delete(Bookings.DELETE_BOOKING.format(response.json()['bookingid']))


class PostTests:

    def test_create_booking(self, response):
        """
        Checks whether new booking is properly created
        """
        assert_that(response.status_code).is_equal_to(200)
        assert_that((HttpManager.get(Bookings.GET_BOOKING.format(response.json()['bookingid']))).status_code).is_equal_to(200)
