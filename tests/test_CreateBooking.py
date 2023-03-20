from pytest import fixture
import json
from pyassert import *

from utils.http_manager import HttpManager
from api.bookings import Bookings


@fixture()
def json_for_create_booking() -> str:
    return json.dumps({
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


@fixture()
def response(json_for_create_booking):
    response = HttpManager.post(Bookings.CREATE_BOOKING, json_for_create_booking)
    yield response
    HttpManager.delete(Bookings.DELETE_BOOKING.format(response.json()['bookingid']))


class PostTests:

    def test_create_booking(self, response):
        """
        Checks whether new booking is properly created
        """
        assert_that(response.status_code).is_equal_to(200)
        assert_that((HttpManager.get(Bookings.GET_BOOKING.format(response.json()['bookingid']))).status_code).is_equal_to(200)
