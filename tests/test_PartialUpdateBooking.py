import json
from pyassert import *

from utils.http_manager import HttpManager
from common.bookings import Bookings

URL = f'{Bookings.BASE_URL}/booking/'
BOOKING = Bookings.get_random_booking()
UPDATE = 'Edited'

# GET Pre-request: Takes booking and its firstname, lastname
get_response = HttpManager.get(URL+str(BOOKING))
get_firstname = get_response.json()['firstname']
get_lastname = get_response.json()['lastname']


def test_partial_update_booking(token, json_for_patch_booking):
    """
    Checks whether partial update properly updates booking data
    """
    patch_response = HttpManager.patch(URL+str(BOOKING), data=json_for_patch_booking)
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(patch_response.json()['firstname']).is_equal_to(json.loads(json_for_patch_booking)['firstname'])
    assert_that(patch_response.json()['lastname']).is_equal_to(json.loads(json_for_patch_booking)['lastname'])
    # Cleans up
    cleaning_data = json.dumps({
        "firstname": "{}".format(get_firstname),
        "lastname": "{}".format(get_lastname)
    })
    HttpManager.patch(URL+str(BOOKING), data=cleaning_data)
