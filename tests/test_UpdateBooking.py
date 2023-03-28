import json
from pyassert import *

from utils.http_manager import HttpManager


class PutTests:

    def test_update_booking(self, existing_booking_url, test_data):
        """
        Checks whether update properly updates booking data
        """
        data = test_data('test_data/update_booking.json')
        response = HttpManager.put(existing_booking_url, data=data)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()['firstname']).is_equal_to(json.loads(data)['firstname'])
