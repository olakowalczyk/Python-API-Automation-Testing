import pytest
import json
from pyassert import *

from utils.http_manager import HttpManager


@pytest.fixture()
def json_for_update_booking():
    return json.dumps({
        "firstname": "Edited",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    })

class TestPut:

    def test_update_booking(self, existing_booking_url, json_for_update_booking):
        """
        Checks whether update properly updates booking data
        """
        response = HttpManager.put(existing_booking_url, data=json_for_update_booking)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()['firstname']).is_equal_to(json.loads(json_for_update_booking)['firstname'])
