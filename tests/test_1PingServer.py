import requests
from pyassert import *
import pytest

URL = 'https://restful-booker.herokuapp.com/ping'


@pytest.mark.ping
def test_ping_server():
    response = requests.get(URL)
    assert_that(response.status_code).is_equal_to(201)
