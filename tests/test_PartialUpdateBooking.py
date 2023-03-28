from pytest import fixture
import json
from pyassert import *

from utils.http_manager import HttpManager


@fixture()
def test_data() -> str:
    with open('test_data/partial_update_booking.json') as data_file:
        data = data_file.read()
        return data


class PatchTests:

    def test_partial_update_booking(self, existing_booking_url, test_data):
        """
        Checks whether partial update properly updates booking data
        """
        response = HttpManager.patch(existing_booking_url, data=test_data)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()['firstname']).is_equal_to(json.loads(test_data)['firstname'])
        assert_that(response.json()['lastname']).is_equal_to(json.loads(test_data)['lastname'])
   