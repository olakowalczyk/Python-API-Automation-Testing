import requests
import json
import jsonpath
import random
from pyassert import *

URL = 'https://restful-booker.herokuapp.com/booking/{}'
BOOKING = random.randrange(1, 10, 1)
UPDATE = 'Edited'

# GET Pre-request: Takes booking and its firstname, lastname
get_response = requests.get(URL.format(BOOKING))
get_response_json = json.loads(get_response.text)
get_firstname = jsonpath.jsonpath(get_response_json, 'firstname')[0]
get_lastname = jsonpath.jsonpath(get_response_json, 'lastname')[0]


def test_update_booking(token):
    # PATCH: Updates booking
    headers = {'Content-Type': 'application/json',
               'Cookie': 'token=' + str(token)}
    patch_data = json.dumps({
        "firstname": "{}".format(UPDATE),
        "lastname": "{}".format(UPDATE)
    })
    patch_response = requests.patch(URL.format(
        BOOKING), data=patch_data, headers=headers)

    # Tests
    patch_response_json = json.loads(patch_response.text)
    patch_firstname = jsonpath.jsonpath(patch_response_json, 'firstname')[0]
    patch_lastname = jsonpath.jsonpath(patch_response_json, 'lastname')[0]
    patch_data_json = json.loads(patch_data)
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(patch_firstname).is_not_equal_to(get_firstname)
    assert_that(patch_lastname).is_not_equal_to(get_lastname)
    assert_that(patch_firstname).is_equal_to(
        jsonpath.jsonpath(patch_data_json, 'firstname')[0])
    assert_that(patch_lastname).is_equal_to(
        jsonpath.jsonpath(patch_data_json, 'lastname')[0])

    # Cleans up
    cleaning_data = json.dumps({
        "firstname": "{}".format(get_firstname),
        "lastname": "{}".format(get_lastname)
    })
    requests.patch(URL.format(
        BOOKING), data=cleaning_data, headers=headers)
