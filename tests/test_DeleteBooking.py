import requests
import pytest
from pyassert import *
from common.bookings import Bookings

URL = f'{Bookings.URL}/booking/'
BOOKING = Bookings.get_random_booking()

# Pre-check: GET booking
if requests.get(URL+str(BOOKING)).status_code == 200:
    # Expected to fail because DELETE returns '201 Created' response instead of '200 OK'
    @pytest.mark.xfail()
    def test_delete_booking(token):
        '''Checks whether booking is properly deleted'''
        # DELETE Request: Deletes booking
        headers = {'Cookie': 'token=' + str(token)}
        response = requests.delete(URL+str(BOOKING), headers=headers)
        # Tests
        assert_that(response.status_code).is_equal_to(200)
        assert_that(requests.get(URL+str(BOOKING)
                                 ).status_code).is_equal_to(404)
else:
    raise Exception('GET pre-request failed')
