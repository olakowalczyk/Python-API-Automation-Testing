from pytest import fixture

from api.bookings import Bookings
from utils.http_manager import HttpManager


@fixture(scope='session', autouse=True)
def token() -> str:
    """
    Returns token which will be used in the test functions 
    that require authentication
    """
    HttpManager.auth(Bookings.AUTH, 'admin', 'password123')
    return HttpManager.headers["Cookie"].split('=')[1]


@fixture()
def existing_booking_url() -> str: 
    booking_id = Bookings.get_random_booking()
    return Bookings.GET_BOOKINGS + booking_id


@fixture()
def test_data():
    def _test_data(data_path):
        with open(data_path) as data_file:
            data = data_file.read()
            return data
    return _test_data