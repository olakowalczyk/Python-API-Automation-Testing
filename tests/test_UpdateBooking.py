import json
from pyassert import *

from utils.http_manager import HttpManager
from common.bookings import Bookings

URL = f'{Bookings.BASE_URL}/booking/'
BOOKING = Bookings.get_random_booking()

# GET Pre-request: Takes booking and its firstname
get_response = HttpManager.get(URL+str(BOOKING))
get_firstname = get_response.json()['firstname']


def test_update_booking(token, json_for_update_booking):
    """
    Checks whether update properly updates booking data
    """
    response = HttpManager.put(URL+str(BOOKING), data=json_for_update_booking)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()['firstname']).is_not_equal_to(get_firstname)
    assert_that(response.json()['firstname']).is_equal_to(json.loads(json_for_update_booking)['firstname'])
    # Cleans up
    cleaning_up_data = json.dumps({
        "firstname": "{}".format(get_firstname),
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    })
    HttpManager.put(URL.format(BOOKING), data=cleaning_up_data)
