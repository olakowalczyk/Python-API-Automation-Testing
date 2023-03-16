import pytest
from pyassert import *

from utils.http_manager import HttpManager
from common.bookings import Bookings

class TestDelete:
    
    booking_id = str(Bookings.get_random_booking())

    # Pre-check: GET booking
    if HttpManager.get(Bookings.GET_BOOKING.format(booking_id)).status_code == 200:
        # Expected to fail because DELETE returns '201 Created' response instead of '200 OK'
        @pytest.mark.xfail()
        def test_delete_booking(self):
            """
            Checks whether booking is properly deleted
            """
            response = HttpManager.delete(Bookings.DELETE_BOOKING.format(booking_id))
            assert_that(response.status_code).is_equal_to(200)
            assert_that(HttpManager.get(Bookings.GET_BOOKING.format(booking_id)
                                    ).status_code).is_equal_to(404)
    else:
        raise Exception('GET pre-request failed')
