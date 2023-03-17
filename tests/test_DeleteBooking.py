from pytest import fixture, mark
from pyassert import *

from utils.http_manager import HttpManager
from api.bookings import Bookings


@fixture()
def booking_id():
    booking_id = Bookings.get_random_booking()
    assert HttpManager.get(Bookings.GET_BOOKING.format(booking_id)).status_code == 200, 'Setup Get pre-request failed'
    return booking_id

class DeleteTests:
    
        @mark.xfail()
        def test_delete_booking(self, booking_id):
            """
            Checks whether booking is properly deleted
            """
            response = HttpManager.delete(Bookings.DELETE_BOOKING.format(booking_id))
            assert_that(response.status_code).is_equal_to(200)
            assert_that(HttpManager.get(Bookings.GET_BOOKING.format(booking_id)
                                    ).status_code).is_equal_to(404)
