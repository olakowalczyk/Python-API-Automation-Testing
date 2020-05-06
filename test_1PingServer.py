import requests
from pyassert import *
import pytest


@pytest.mark.ping
def test_ping_server():
    url = 'https://restful-booker.herokuapp.com/ping'
    response = requests.get(url)

    assert_that(response.status_code).is_equal_to(201)
