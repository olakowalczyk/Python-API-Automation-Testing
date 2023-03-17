from pytest import fixture
import json
from pyassert import *

from utils.http_manager import HttpManager


@fixture()
def json_for_patch_booking():
    return json.dumps({
        "firstname": "{}".format('Edited'),
        "lastname": "{}".format('Edited')
    })


class PatchTests:

    def test_partial_update_booking(self, existing_booking_url, json_for_patch_booking):
        """
        Checks whether partial update properly updates booking data
        """
        response = HttpManager.patch(existing_booking_url, data=json_for_patch_booking)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()['firstname']).is_equal_to(json.loads(json_for_patch_booking)['firstname'])
        assert_that(response.json()['lastname']).is_equal_to(json.loads(json_for_patch_booking)['lastname'])
   