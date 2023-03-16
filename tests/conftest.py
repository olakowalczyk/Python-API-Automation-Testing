import pytest
import json

from common.bookings import Bookings
from utils.http_manager import HttpManager


@pytest.fixture(autouse=True)
def token() -> str:
    """
    Returns token which will be used in the test functions 
    that require authentication
    """
    HttpManager.auth(Bookings.AUTH, 'admin', 'password123')
    return HttpManager.headers["Cookie"].split('=')[1]


@pytest.fixture()
def existing_booking_url() -> str: 
    booking_id = Bookings.get_random_booking()
    return Bookings.GET_BOOKINGS + booking_id


@pytest.fixture()
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
