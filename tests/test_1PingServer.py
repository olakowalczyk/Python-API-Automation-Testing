from pytest import mark
from pyassert import *

from utils.http_manager import HttpManager
from api.bookings import Bookings


class ServerTests:

    @mark.ping
    def test_ping_server(self):
        """
        Checks whether server is running
        """
        response = HttpManager.get(Bookings.PING)
        assert_that(response.status_code).is_equal_to(201)
