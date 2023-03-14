import pytest

from common.bookings import Bookings
from utils.http_manager import HttpManager


@pytest.fixture()
def token():
    """
    Returns token which will be used (as a fixture) 
    in the test functions that require authentication
    """
    HttpManager.auth(f'{Bookings.BASE_URL}/auth', 'admin', 'password123')
    return HttpManager.headers["Cookie"]

