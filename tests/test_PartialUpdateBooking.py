import json
from pyassert import *

from utils.http_manager import HttpManager


class PatchTests:

    def test_partial_update_booking(self, existing_booking_url, test_data):
        """
        Checks whether partial update properly updates booking data
        """
        data = test_data('test_data/partial_update_booking.json')
        response = HttpManager.patch(existing_booking_url, data=data)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()['firstname']).is_equal_to(json.loads(data)['firstname'])
        assert_that(response.json()['lastname']).is_equal_to(json.loads(data)['lastname'])
   