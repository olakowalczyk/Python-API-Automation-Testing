import pytest
from pyassert import *

from utils.http_manager import HttpManager
from common.bookings import Bookings

URL = f'{Bookings.BASE_URL}/booking/'
BOOKING = Bookings.get_random_booking()

# Pre-check: GET booking
if HttpManager.get(URL+str(BOOKING)).status_code == 200:
    # Expected to fail because DELETE returns '201 Created' response instead of '200 OK'
    @pytest.mark.xfail()
    def test_delete_booking(token):
        """
        Checks whether booking is properly deleted
        """
        response = HttpManager.delete(URL+str(BOOKING))
        assert_that(response.status_code).is_equal_to(200)
        assert_that(HttpManager.get(URL+str(BOOKING)
                                 ).status_code).is_equal_to(404)
else:
    raise Exception('GET pre-request failed')
