import pytest
import requests
from pyassert import *

from common.bookings import Bookings


URL = f'{Bookings.URL}/ping'


@pytest.mark.ping
def test_ping_server():
    '''Checks whether server is running'''
    response = requests.get(URL)
    assert_that(response.status_code).is_equal_to(201)
