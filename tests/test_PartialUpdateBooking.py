import requests
import json
from pyassert import *
from common.bookings import Bookings

URL = 'https://restful-booker.herokuapp.com/booking/{}'
BOOKING = Bookings.get_random_booking()
UPDATE = 'Edited'

# GET Pre-request: Takes booking and its firstname, lastname
get_response = requests.get(URL.format(BOOKING))
get_firstname = get_response.json()['firstname']
get_lastname = get_response.json()['lastname']


def test_partial_update_booking(token):
    '''Checks whether partial update properly updates booking data'''
    # PATCH request: Updates booking
    headers = {'Content-Type': 'application/json',
               'Cookie': 'token=' + str(token)}
    patch_data = json.dumps({
        "firstname": "{}".format(UPDATE),
        "lastname": "{}".format(UPDATE)
    })
    patch_data_json = json.loads(patch_data)
    patch_response = requests.patch(URL.format(
        BOOKING), data=patch_data, headers=headers)
    patch_firstname = patch_response.json()['firstname']
    patch_lastname = patch_response.json()['lastname']
    # Tests
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(patch_firstname).is_not_equal_to(get_firstname)
    assert_that(patch_lastname).is_not_equal_to(get_lastname)
    assert_that(patch_firstname).is_equal_to(patch_data_json['firstname'])
    assert_that(patch_lastname).is_equal_to(patch_data_json['lastname'])
    # Cleans up
    cleaning_data = json.dumps({
        "firstname": "{}".format(get_firstname),
        "lastname": "{}".format(get_lastname)
    })
    requests.patch(URL.format(
        BOOKING), data=cleaning_data, headers=headers)
