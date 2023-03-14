import pytest
from pyassert import *

from utils.http_manager import HttpManager
from common.bookings import Bookings


@pytest.mark.ping
def test_ping_server():
    """
    Checks whether server is running
    """
    response = HttpManager.get(f'{Bookings.BASE_URL}/ping')
    assert_that(response.status_code).is_equal_to(201)
